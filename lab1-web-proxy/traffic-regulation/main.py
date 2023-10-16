import grpc
from concurrent import futures
import traffic_regulation_pb2
import traffic_regulation_pb2_grpc
import psycopg2.pool
import threading
import requests


def register_service(service_name, service_host, service_port, service_discovery_endpoint):
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
            print(f"Registered {service_name} with service discovery")
        else:
            print(f"Failed to register {service_name} with service discovery: {response.status_code}")
    except Exception as e:
        print(f"Error while registering {service_name}: {str(e)}")


try:
    conn = psycopg2.connect(
        dbname='traffic-regulation-db',
        user='postgres',
        password='397777',
        host='localhost',
        port='5432'
    )
    print("Connection to the traffic regulation database is successful!")
    conn.close()
except Exception as e:
    print(f"Error connecting to the traffic regulation database: {e}")

db_pool = psycopg2.pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    dbname='traffic-regulation-db',
    user='postgres',
    password='397777',
    host='localhost',
    port='5432'
)


class TrafficRegulationServicer(traffic_regulation_pb2_grpc.TrafficRegulationServicer):
    def ReceiveDataForLogs(self, request, context):
        print("New request for receiving data.")

        timeout_seconds = 2

        timeout_event = threading.Event()

        def timeout_handler():
            timeout_event.set()
            print("Request timed out.")

        timer_thread = threading.Timer(timeout_seconds, timeout_handler)
        timer_thread.start()

        # time.sleep(3)

        if timeout_event.is_set():
            print("Request timed out before database operation.")
            context.set_code(grpc.StatusCode.DEADLINE_EXCEEDED)
            context.set_details("Request timed out before database operation.")
            return traffic_regulation_pb2.TrafficDataForLogsReceiveResponse(message="Request timed out before database "
                                                                                    "operation.")

        try:
            conn = db_pool.getconn()
            with conn.cursor() as cursor:
                # time.sleep(3)

                if timeout_event.is_set():
                    print("Request timed out before inserting data.")
                    context.set_code(grpc.StatusCode.DEADLINE_EXCEEDED)
                    context.set_details("Request timed out before inserting data.")
                    return traffic_regulation_pb2.TrafficDataForLogsReceiveResponse(message="Request timed out before "
                                                                                            "inserting data.")

                insert_query = """
                    INSERT INTO traffic_data (intersection_id, date, time, signal_status, vehicle_count, incident)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """
                cursor.execute(insert_query, (
                    request.intersection_id,
                    request.date,
                    request.time,
                    request.signal_status_1,
                    request.vehicle_count,
                    request.incident,
                ))
                conn.commit()

            with conn.cursor() as cursor:
                # time.sleep(3)

                if timeout_event.is_set():
                    print("Request timed out before inserting data.")
                    context.set_code(grpc.StatusCode.DEADLINE_EXCEEDED)
                    context.set_details("Request timed out before inserting data.")
                    return traffic_regulation_pb2.TrafficDataForLogsReceiveResponse(message="Request timed out before "
                                                                                            "inserting data.")
                cursor.execute(
                    """
                    SELECT log_messages FROM traffic_logs
                    WHERE intersection_id = %s AND date = %s
                    """,
                    (request.intersection_id, request.date),
                )
                existing_logs = cursor.fetchone()

                if existing_logs is not None:
                    existing_log_messages = existing_logs[0]
                else:
                    existing_log_messages = []

                if request.signal_status_1 == 1 and request.vehicle_count > 30:
                    request.signal_status_1 = 2
                    log_message = (f"Traffic light at intersection nr.{request.intersection_id} changed to 'green' due "
                                   f"to high vehicle count.")

                    existing_log_messages.append(log_message)

                if request.signal_status_1 == 2 and request.vehicle_count < 5:
                    request.signal_status_1 = 1

                    log_message = (f"Traffic light at intersection nr.{request.intersection_id} changed to 'red' due "
                                   f"to low vehicle count.")

                    existing_log_messages.append(log_message)

                cursor.execute(
                    """
                    INSERT INTO traffic_logs (intersection_id, date, log_messages)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (intersection_id, date)
                    DO UPDATE
                    SET log_messages = %s
                    """,
                    (request.intersection_id, request.date, existing_log_messages,
                     existing_log_messages),
                )

                conn.commit()
                timer_thread.cancel()
            response = traffic_regulation_pb2.TrafficDataForLogsReceiveResponse()
            response.message = f"Traffic data for intersection nr.{request.intersection_id} received successfully."
            db_pool.putconn(conn)
        except Exception as e:
            response = traffic_regulation_pb2.TrafficDataForLogsReceiveResponse()
            response.message = f"Error saving traffic data: {str(e)}"
        except grpc.RpcError as e:
            print(f"RPC error: {str(e)}")
            context.set_code(e.code())
            context.set_details(str(e))
            response = traffic_regulation_pb2.TrafficDataForLogsReceiveResponse(message=str(e))

        return response


def start():
    service_name = "traffic-regulation-service"
    service_host = "localhost"
    service_port = 8081
    service_discovery_endpoint = "http://localhost:9090"

    register_service(service_name, service_host, service_port, service_discovery_endpoint)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    traffic_regulation_pb2_grpc.add_TrafficRegulationServicer_to_server(TrafficRegulationServicer(), server)
    server.add_insecure_port("localhost:8081")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    start()
