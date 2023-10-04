import grpc
import traffic_pb2
import traffic_pb2_grpc


def receive_data():
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = traffic_pb2_grpc.TrafficAnalyzerStub(channel)
        request = traffic_pb2.TrafficData(
            intersection_id=5,
            signal_status_1=1,
            vehicle_count=35,
            incident=False,
            date="04.05.2023",
            time="14:03"
        )
        response = stub.ReceiveData(request)
        print(response.message)


def get_today_statistics(intersection_id):
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = traffic_pb2_grpc.TrafficAnalyzerStub(channel)
        request = traffic_pb2.IntersectionRequest(intersection_id=intersection_id)
        response = stub.GetTodayStatistics(request)
        print("Today's Statistics: ")
        print("Intersection ID:", response.intersection_id)
        print("Timestamp:", response.timestamp)
        print("Average Vehicle Count:", response.average_vehicle_count)
        print("Traffic Density:", response.traffic_density)
        print("Peak Hours:", response.peak_hours)
        print("Incidents:", response.incidents)


def get_last_week_statistics(intersection_id):
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = traffic_pb2_grpc.TrafficAnalyzerStub(channel)
        request = traffic_pb2.IntersectionRequest(intersection_id=intersection_id)
        response = stub.GetLastWeekStatistics(request)
        print("Last Week's Statistics: ")
        print("Intersection ID:", response.intersection_id)
        print("Timestamp:", response.timestamp)
        print("Average Vehicle Count:", response.average_vehicle_count)
        print("Traffic Density:", response.traffic_density)
        print("Peak Hours:", response.peak_hours)
        print("Incidents:", response.incidents)


def get_next_week_predictions(intersection_id):
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = traffic_pb2_grpc.TrafficAnalyzerStub(channel)
        request = traffic_pb2.IntersectionRequest(intersection_id=intersection_id)
        response = stub.GetNextWeekPredictions(request)
        print("Next Week's Predictions: ")
        print("Intersection ID:", response.intersection_id)
        print("Timestamp:", response.timestamp)
        print("Average Vehicle Count:", response.average_vehicle_count)
        print("Traffic Density:", response.traffic_density)
        print("Peak Hours:", response.peak_hours)
        print("Incidents:", response.incidents)


if __name__ == '__main__':
    receive_data()
    get_today_statistics(5)
    get_last_week_statistics(5)
    get_next_week_predictions(5)
