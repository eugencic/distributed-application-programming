import grpc
import traffic_regulation_pb2
import traffic_regulation_pb2_grpc
from concurrent import futures
import threading
from threading import Timer
import requests
import time
from cachetools import TTLCache

service_discovery_endpoint = "http://localhost:9090"
load_balancer_name = "traffic-regulation-load-balancer"
load_balancer_host = "localhost"
load_balancer_port = 8000
number_of_replicas = 3
replica_addresses = []
current_replica_index = 0
lock = threading.Lock()


def register_load_balancer(service_name, service_host, service_port):
    service_data = {
        "name": service_name,
        "host": service_host,
        "port": service_port,
    }
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.post(
            f"{service_discovery_endpoint}/register_service",
            json=service_data,
            headers=headers,
        )
        if response.status_code == 201:
            print(f"Registered {service_name} with service discovery.")
        else:
            print(f"Failed to register {service_name} with service discovery: {response.status_code}")
    except Exception as e:
        print(f"Error while registering {service_name}: {str(e)}")


def get_service_info(service_name):
    try:
        response = requests.get(f"{service_discovery_endpoint}/get_service_data?name={service_name}")
        if response.status_code == 200:
            response = response.json()
            response = [response["name"], response["host"], response["port"]]
            return response
        else:
            print(f"Failed to fetch replica addresses: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error while fetching replica addresses: {str(e)}")
        return []


def get_next_replica():
    global current_replica_index
    with lock:
        current_replica_index = (current_replica_index + 1) % len(replica_addresses)
        return current_replica_index


def print_problematic_service(replica_number):
    print(f"Service at replica nr.{replica_number} is problematic. Consider taking action.")


cache = TTLCache(maxsize=1000, ttl=60)


class LoadBalancerCircuitBreaker:
    def __init__(self, error_threshold, time_window, timeout):
        self.error_threshold = error_threshold
        self.time_window = time_window
        self.timeout = timeout
        self.replica_errors = {}
        self.timer = Timer(self.timeout, self.cleanup_all_errors)

    def start_timer(self):
        self.timer.start()

    def cleanup_all_errors(self):
        for replica_number in self.replica_errors:
            now = time.time()
            self.replica_errors[replica_number] = [error for error in self.replica_errors[replica_number] if
                                                   now - error <= self.time_window]
        self.timer = Timer(self.timeout, self.cleanup_all_errors)
        self.timer.start()

    def __call__(self, func):
        def wrapper(request, context, method):
            try:
                if method in ["GetTodayControlLogs", "GetLastWeekControlLogs"]:
                    cache_key = (method, request.intersection_id)
                    cached_data = cache.get(cache_key)
                    if cached_data is not None:
                        print("Cache is present...")
                        return cached_data
                print("Cache is not present...")
                response = func(request, context, method)
                replica_number = current_replica_index + 1
                print(f"Successful request at replica nr.{replica_number}.")
                if method in ["GetTodayControlLogs", "GetLastWeekControlLogs"]:
                    print("Storing cache...")
                    cache[cache_key] = response
                return response
            except grpc.RpcError as e:
                replica_number = current_replica_index + 1
                if replica_number not in self.replica_errors:
                    self.replica_errors[replica_number] = []
                self.replica_errors[replica_number].append(time.time())
                print(f"Unsuccessful request at replica nr.{replica_number}.")
                self.cleanup_old_errors(replica_number)
                if len(self.replica_errors[replica_number]) >= self.error_threshold:
                    print_problematic_service(replica_number)

        return wrapper

    def cleanup_old_errors(self, replica_number):
        now = time.time()
        self.replica_errors[replica_number] = [error for error in self.replica_errors[replica_number] if
                                               now - error <= self.time_window]


circuit_breaker = LoadBalancerCircuitBreaker(error_threshold=3, time_window=35, timeout=30)
circuit_breaker.start_timer()


@circuit_breaker
def forward_request(request, context, method):
    next_replica_index = get_next_replica()
    channel = grpc.insecure_channel(replica_addresses[next_replica_index])
    stub = traffic_regulation_pb2_grpc.TrafficRegulationStub(channel)
    if method == "ReceiveDataForLogs":
        response = stub.ReceiveDataForLogs(request)
    elif method == "GetTodayControlLogs":
        response = stub.GetTodayControlLogs(request)
    elif method == "GetLastWeekControlLogs":
        response = stub.GetLastWeekControlLogs(request)
    else:
        context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
        context.set_details(f"Invalid method: {method}")
        response = traffic_regulation_pb2.TrafficRegulationResponse(logs=[f"Invalid method: {method}"])
    return response


def collect_status_from_replicas():
    responses = []
    for replica_address in replica_addresses:
        channel = grpc.insecure_channel(replica_address)
        stub = traffic_regulation_pb2_grpc.TrafficRegulationStub(channel)
        try:
            response = stub.TrafficRegulationServiceStatus(
                traffic_regulation_pb2.TrafficRegulationServiceStatusRequest())
            responses.append(response.message)
        except Exception as e:
            print(f"Error getting status from replica {replica_address}: {str(e)}")
    return responses


def merge_status_responses(responses):
    merged_status = ", ".join(response for response in responses)
    return merged_status


class LoadBalancerServicer(traffic_regulation_pb2_grpc.TrafficRegulationServicer):
    def __init__(self):
        pass

    def ReceiveDataForLogs(self, request, context):
        response = forward_request(request, context, "ReceiveDataForLogs")
        return response

    def GetTodayControlLogs(self, request, context):
        response = forward_request(request, context, "GetTodayControlLogs")
        return response

    def GetLastWeekControlLogs(self, request, context):
        response = forward_request(request, context, "GetLastWeekControlLogs")
        return response

    def TrafficRegulationServiceStatus(self, request, context):
        responses = collect_status_from_replicas()
        merged_response = merge_status_responses(responses)
        unhealthy_service = "unhealthy"
        if unhealthy_service in str(merged_response):
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"One or more services experience troubles. Statuses: {str(merged_response)}")
            response = traffic_regulation_pb2.TrafficRegulationServiceStatusResponse(
                message=f"Statuses: {str(merged_response)}")
            return response
        else:
            context.set_code(grpc.StatusCode.OK)
            response = traffic_regulation_pb2.TrafficRegulationServiceStatusResponse(
                message=f"All service replicas are healthy. Statuses: {str(merged_response)}")
            return response


def start_load_balancer(host, port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    traffic_regulation_pb2_grpc.add_TrafficRegulationServicer_to_server(LoadBalancerServicer(), server)
    server.add_insecure_port(f"{host}:{port}")
    server.start()
    print(f"Load balancer {load_balancer_name} listening on port {port}...")
    register_load_balancer(load_balancer_name, host, port)
    for i in range(number_of_replicas):
        replica = get_service_info(f"traffic-regulation-service-{i + 1}")
        replica = "" + str(replica[1]) + ":" + str(replica[2])
        print(f"{load_balancer_name}-{i + 1} registered.")
        replica_addresses.append(replica)
    server.wait_for_termination()


if __name__ == '__main__':
    start_load_balancer(load_balancer_host, load_balancer_port)
