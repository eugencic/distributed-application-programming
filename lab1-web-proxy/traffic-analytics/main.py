import grpc
from concurrent import futures
import traffic_pb2
import traffic_pb2_grpc
import psycopg2.pool
from datetime import datetime

print("Starting the server...")

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


class TrafficAnalyzerServicer(traffic_pb2_grpc.TrafficAnalyzerServicer):
    def ReceiveData(self, request, context):
        print("New upcoming data: ")
        print(request)
        response = traffic_pb2.TrafficDataReceiveResponse()
        response.message = f"Traffic data for intersection nr.{request.intersection_id} received successfully."
        return response

    def GetTodayStatistics(self, request, context):
        response = traffic_pb2.TrafficAnalytics(
            intersection_id=request.intersection_id,
            timestamp=datetime.now().isoformat(),
            average_vehicle_count=45.0,
            traffic_density="Moderate",
            peak_hours=["07:00 AM - 09:00 AM"],
            incidents=1
        )
        return response

    def GetLastWeekStatistics(self, request, context):
        response = traffic_pb2.TrafficAnalytics(
            intersection_id=request.intersection_id,
            timestamp=datetime.now().isoformat(),
            average_vehicle_count=40.0,
            traffic_density="Low",
            peak_hours=["08:00 AM - 10:00 AM"],
            incidents=0
        )
        return response

    def GetNextWeekPredictions(self, request, context):
        response = traffic_pb2.TrafficAnalytics(
            intersection_id=request.intersection_id,
            timestamp=datetime.now().isoformat(),
            average_vehicle_count=50.0,
            traffic_density="Moderate",
            peak_hours=["07:30 AM - 09:30 AM"],
            incidents=2
        )
        return response


def start():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    traffic_pb2_grpc.add_TrafficAnalyzerServicer_to_server(TrafficAnalyzerServicer(), server)
    server.add_insecure_port("localhost:8080")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    start()
