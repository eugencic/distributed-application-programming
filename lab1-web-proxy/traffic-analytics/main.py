import grpc
from concurrent import futures
import traffic_analytics_pb2
import traffic_analytics_pb2_grpc
import psycopg2.pool
from dateutil.relativedelta import relativedelta
from datetime import datetime
import threading
import requests
import sys


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
            print(f"Registered {service_name} with service discovery.")
        else:
            print(f"Failed to register {service_name} with service discovery: {response.status_code}")
    except Exception as e:
        print(f"Error while registering {service_name}: {str(e)}")


try:
    conn = psycopg2.connect(
        dbname='traffic-analytics-db',
        user='postgres',
        password='397777',
        host='localhost',
        port='5432'
    )
    print("Connection to the traffic analytics database is successful!")
    conn.close()
except Exception as e:
    print(f"Error connecting to the traffic analytics database: {e}")

db_pool = psycopg2.pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    dbname='traffic-analytics-db',
    user='postgres',
    password='397777',
    host='localhost',
    port='5432'
)


class TrafficAnalyticsServicer(traffic_analytics_pb2_grpc.TrafficAnalyticsServicer):
    def ReceiveDataForAnalytics(self, request, context):
        print("New request for receiving data.")
        timeout_seconds = 2
        timeout_event = threading.Event()

        def timeout_handler():
            timeout_event.set()
            print("Timer is set.")

        timer_thread = threading.Timer(timeout_seconds, timeout_handler)
        timer_thread.start()
        # time.sleep(3)
        if timeout_event.is_set():
            print("Request timed out before database operation.")
            context.set_code(grpc.StatusCode.DEADLINE_EXCEEDED)
            context.set_details("Request timed out before database operation.")
            return traffic_analytics_pb2.TrafficDataForAnalyticsReceiveResponse(message="Request timed out before "
                                                                                        "database operation.")
        try:
            conn = db_pool.getconn()
            with conn.cursor() as cursor:
                # time.sleep(3)
                if timeout_event.is_set():
                    print("Request timed out before inserting data.")
                    context.set_code(grpc.StatusCode.DEADLINE_EXCEEDED)
                    context.set_details("Request timed out before inserting data.")
                    return traffic_analytics_pb2.TrafficDataForAnalyticsReceiveResponse(message="Request timed out "
                                                                                                "before inserting "
                                                                                                "data.")
                insert_query = """
                    INSERT INTO traffic_data (intersection_id, date, time, signal_status_1, vehicle_count, incident)
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
                timer_thread.cancel()
            response = traffic_analytics_pb2.TrafficDataForAnalyticsReceiveResponse()
            response.message = f"Traffic data for intersection nr.{request.intersection_id} received successfully."
            db_pool.putconn(conn)
        except Exception as e:
            response = traffic_analytics_pb2.TrafficDataForAnalyticsReceiveResponse()
            response.message = f"Error saving traffic data: {str(e)}"
        except grpc.RpcError as e:
            print(f"RPC error: {str(e)}")
            context.set_code(e.code())
            context.set_details(str(e))
            response = traffic_analytics_pb2.TrafficDataForAnalyticsReceiveResponse(message=str(e))
        return response

    def GetTodayStatistics(self, request, context):
        print("New request for daily statistics.")
        timeout_seconds = 2
        timeout_event = threading.Event()

        def timeout_handler():
            timeout_event.set()
            print("Timer is set.")

        timer_thread = threading.Timer(timeout_seconds, timeout_handler)
        timer_thread.start()
        # time.sleep(3)
        if timeout_event.is_set():
            print("Request timed out before database operation.")
            context.set_code(grpc.StatusCode.DEADLINE_EXCEEDED)
            context.set_details("Request timed out before database operation.")
            return traffic_analytics_pb2.TrafficDataForAnalyticsReceiveResponse(message="Request timed out before "
                                                                                        "database operation.")
        try:
            conn = db_pool.getconn()
            with conn.cursor() as cursor:
                query = """
                SELECT vehicle_count, time, incident from traffic_data
                WHERE intersection_id = %s
                AND date = %s
                """
                cursor.execute(query, (request.intersection_id, datetime.now().strftime('%Y-%m-%d')))
                results = cursor.fetchall()
                print("Retrieved data:", results)
                total_vehicle_count = 0
                total_incidents = 0
                times = [result[1] for result in results]
                for result in results:
                    total_vehicle_count += result[0]
                    if result[2]:
                        total_incidents += 1
                    sorted_times = sorted(times)
                peak_start = sorted_times[0].strftime("%I:%M %p")
                peak_end = sorted_times[-1].strftime("%I:%M %p")
                peak_hours = f"{peak_start} - {peak_end}"
                average_vehicle_count = round(total_vehicle_count / len(results), 3) if len(results) > 0 else 0.0
                average_incidents = round(total_incidents / len(results), 3) if len(results) > 0 else 0.0
            with conn.cursor() as cursor:
                # time.sleep(3)
                if timeout_event.is_set():
                    print("Request timed out before inserting data.")
                    context.set_code(grpc.StatusCode.DEADLINE_EXCEEDED)
                    context.set_details("Request timed out before inserting data.")
                    return traffic_analytics_pb2.TrafficDataForAnalyticsReceiveResponse(message="Request timed out "
                                                                                                "before inserting "
                                                                                                "data.")
                query = """
                    INSERT INTO traffic_analytics (
                    intersection_id, 
                    date, 
                    average_vehicle_count, 
                    average_incidents, 
                    analytics_type
                    )
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (intersection_id, date, analytics_type)
                    DO UPDATE SET
                      average_vehicle_count = EXCLUDED.average_vehicle_count,
                      average_incidents = EXCLUDED.average_incidents;
                """
                try:
                    cursor.execute(query, (
                        request.intersection_id,
                        datetime.now().strftime("%Y-%m-%d"),
                        average_vehicle_count,
                        average_incidents,
                        'Daily'
                    ))
                    conn.commit()
                    timer_thread.cancel()
                except Exception as e:
                    print("Error inserting data into traffic_analytics:", e)
            response = traffic_analytics_pb2.TrafficAnalyticsResponse()
            response.intersection_id = request.intersection_id
            response.timestamp = datetime.now().isoformat()
            response.average_vehicle_count = average_vehicle_count
            response.peak_hours = peak_hours
            response.average_incidents = average_incidents
            db_pool.putconn(conn)
            return response
        except Exception as e:
            response = traffic_analytics_pb2.TrafficAnalyticsResponse()
            response.intersection_id = 0
            response.timestamp = '0'
            response.average_vehicle_count = 0
            response.peak_hours = '0'
            response.average_incidents = 0
            return response
        except grpc.RpcError as e:
            print(f"RPC error: {str(e)}")
            context.set_code(e.code())
            context.set_details(str(e))
            response = traffic_analytics_pb2.TrafficDataForAnalyticsReceiveResponse(message=str(e))
            return response

    def GetLastWeekStatistics(self, request, context):
        print("New request for weekly statistics.")
        timeout_seconds = 2
        timeout_event = threading.Event()

        def timeout_handler():
            timeout_event.set()
            print("Timer is set.")

        timer_thread = threading.Timer(timeout_seconds, timeout_handler)
        timer_thread.start()
        # time.sleep(3)
        if timeout_event.is_set():
            print("Request timed out before database operation.")
            context.set_code(grpc.StatusCode.DEADLINE_EXCEEDED)
            context.set_details("Request timed out before database operation.")
            return traffic_analytics_pb2.TrafficDataForAnalyticsReceiveResponse(message="Request timed out before "
                                                                                        "database operation.")
        try:
            conn = db_pool.getconn()
            with conn.cursor() as cursor:
                end_date = datetime.now().date()
                start_date = end_date - relativedelta(weeks=1)
                insert_date = end_date
                query = """
                SELECT vehicle_count, time, incident from traffic_data
                WHERE intersection_id = %s
                AND date >= %s 
                AND date <= %s
                """
                cursor.execute(query, (
                    request.intersection_id, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')
                ))
                results = cursor.fetchall()
                print("Retrieved data for the last week:", results)
                total_vehicle_count = 0
                total_incidents = 0
                times = [result[1] for result in results]
                for result in results:
                    total_vehicle_count += result[0]
                    if result[2]:
                        total_incidents += 1
                    sorted_times = sorted(times)
                peak_start = sorted_times[0].strftime("%I:%M %p")
                peak_end = sorted_times[-1].strftime("%I:%M %p")
                peak_hours = f"{peak_start} - {peak_end}"
                average_vehicle_count = round(total_vehicle_count / len(results), 3) if len(results) > 0 else 0.0
                average_incidents = round(total_incidents / len(results), 3) if len(results) > 0 else 0.0
            with conn.cursor() as cursor:
                # time.sleep(3)
                if timeout_event.is_set():
                    print("Request timed out before inserting data.")
                    context.set_code(grpc.StatusCode.DEADLINE_EXCEEDED)
                    context.set_details("Request timed out before inserting data.")
                    return traffic_analytics_pb2.TrafficDataForAnalyticsReceiveResponse(message="Request timed out "
                                                                                                "before inserting "
                                                                                                "data.")
                query = """
                    INSERT INTO traffic_analytics (
                        intersection_id, 
                        date, 
                        average_vehicle_count, 
                        average_incidents, 
                        analytics_type
                    )
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (intersection_id, date, analytics_type)
                    DO UPDATE SET
                        average_vehicle_count = EXCLUDED.average_vehicle_count,
                        average_incidents = EXCLUDED.average_incidents;
                """
                try:
                    cursor.execute(query, (
                        request.intersection_id,
                        insert_date.strftime("%Y-%m-%d"),
                        average_vehicle_count,
                        average_incidents,
                        'Weekly'
                    ))
                    conn.commit()
                    timer_thread.cancel()
                except Exception as e:
                    print("Error inserting data into traffic_analytics:", e)
            response = traffic_analytics_pb2.TrafficAnalyticsResponse()
            response.intersection_id = request.intersection_id
            response.timestamp = datetime.now().isoformat()
            response.average_vehicle_count = average_vehicle_count
            response.peak_hours = peak_hours
            response.average_incidents = average_incidents
            db_pool.putconn(conn)
            return response
        except Exception as e:
            response = traffic_analytics_pb2.TrafficAnalyticsResponse()
            response.intersection_id = 0
            response.timestamp = '0'
            response.average_vehicle_count = 0
            response.peak_hours = '0'
            response.average_incidents = 0
            return response
        except grpc.RpcError as e:
            print(f"RPC error: {str(e)}")
            context.set_code(e.code())
            context.set_details(str(e))
            response = traffic_analytics_pb2.TrafficDataForAnalyticsReceiveResponse(message=str(e))
            return response

    def GetNextWeekPredictions(self, request, context):
        print("New request for next week predictions.")
        timeout_seconds = 2
        timeout_event = threading.Event()

        def timeout_handler():
            timeout_event.set()
            print("Timer is set.")

        timer_thread = threading.Timer(timeout_seconds, timeout_handler)
        timer_thread.start()
        # time.sleep(3)
        if timeout_event.is_set():
            print("Request timed out before database operation.")
            context.set_code(grpc.StatusCode.DEADLINE_EXCEEDED)
            context.set_details("Request timed out before database operation.")
            return traffic_analytics_pb2.TrafficDataForAnalyticsReceiveResponse(message="Request timed out before "
                                                                                        "database operation.")
        try:
            conn = db_pool.getconn()
            with conn.cursor() as cursor:
                end_date = datetime.now().date()
                start_date = end_date - relativedelta(weeks=1)
                insert_date = end_date
                query = """
                SELECT vehicle_count, time, incident from traffic_data
                WHERE intersection_id = %s
                AND date >= %s 
                AND date <= %s
                """
                cursor.execute(query, (
                    request.intersection_id, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')
                ))
                results = cursor.fetchall()
                print("Retrieved data for the last week for predictions:", results)
                total_vehicle_count = 0
                total_incidents = 0
                times = [result[1] for result in results]
                for result in results:
                    total_vehicle_count += result[0]
                    if result[2]:
                        total_incidents += 1
                    sorted_times = sorted(times)
                peak_start = sorted_times[0].strftime("%I:%M %p")
                peak_end = sorted_times[-1].strftime("%I:%M %p")
                peak_hours = f"{peak_start} - {peak_end}"
                average_vehicle_count = round(total_vehicle_count / len(results), 3) if len(results) > 0 else 0.0
                average_incidents = round(total_incidents / len(results), 3) if len(results) > 0 else 0.0
                predicted_average_vehicle_count = average_vehicle_count + 10
                predicted_average_incidents = average_incidents + 10
            with conn.cursor() as cursor:
                # time.sleep(3)
                if timeout_event.is_set():
                    print("Request timed out before inserting data.")
                    context.set_code(grpc.StatusCode.DEADLINE_EXCEEDED)
                    context.set_details("Request timed out before inserting data.")
                    return traffic_analytics_pb2.TrafficDataForAnalyticsReceiveResponse(message="Request timed out "
                                                                                                "before inserting "
                                                                                                "data.")
                query = """
                    INSERT INTO traffic_analytics (
                        intersection_id, 
                        date, 
                        average_vehicle_count, 
                        average_incidents, 
                        analytics_type
                    )
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT (intersection_id, date, analytics_type)
                    DO UPDATE SET
                        average_vehicle_count = EXCLUDED.average_vehicle_count,
                        average_incidents = EXCLUDED.average_incidents;
                """
                try:
                    cursor.execute(query, (
                        request.intersection_id,
                        insert_date.strftime("%Y-%m-%d"),
                        predicted_average_vehicle_count,
                        predicted_average_incidents,
                        'Prediction'
                    ))
                    conn.commit()
                    timer_thread.cancel()
                except Exception as e:
                    print("Error inserting data into traffic_analytics:", e)
            response = traffic_analytics_pb2.TrafficAnalyticsResponse()
            response.intersection_id = request.intersection_id
            response.timestamp = datetime.now().isoformat()
            response.average_vehicle_count = predicted_average_vehicle_count
            response.peak_hours = peak_hours
            response.average_incidents = predicted_average_incidents
            db_pool.putconn(conn)
            return response
        except Exception as e:
            response = traffic_analytics_pb2.TrafficAnalyticsResponse()
            response.intersection_id = 0
            response.timestamp = '0'
            response.average_vehicle_count = 0
            response.peak_hours = '0'
            response.average_incidents = 0
            return response
        except grpc.RpcError as e:
            print(f"RPC error: {str(e)}")
            context.set_code(e.code())
            context.set_details(str(e))
            response = traffic_analytics_pb2.TrafficDataForAnalyticsReceiveResponse(message=str(e))
            return response


output_lock = threading.Lock()
registration_lock = threading.Lock()


def safe_print(message):
    with output_lock:
        print(message)


def start_server(name, host, port, service_discovery):
    try:
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        traffic_analytics_pb2_grpc.add_TrafficAnalyticsServicer_to_server(TrafficAnalyticsServicer(), server)
        server.add_insecure_port(f"{host}:{port}")
        with registration_lock:
            register_service(name, host, port, service_discovery)
            safe_print(f"{name} listening on port {port}...")
        server.start()
        server.wait_for_termination()
    except Exception as e:
        print(f"Error starting server {name} on port {port}: {str(e)}")
        sys.exit(1)


if __name__ == '__main__':
    service_discovery_endpoint = "http://localhost:9090"
    num_replicas = 3
    service_host = "localhost"
    service_base_port = 8000
    replica_ports = [service_base_port + i for i in range(num_replicas)]
    replica_threads = []
    for i, port in enumerate(replica_ports):
        service_name = f"traffic-analytics-service-{i + 1}"
        service_port = port
        replica_thread = threading.Thread(target=start_server,
                                          args=(service_name, service_host, service_port, service_discovery_endpoint))
        replica_threads.append(replica_thread)
    for thread in replica_threads:
        thread.start()
    for thread in replica_threads:
        thread.join()

