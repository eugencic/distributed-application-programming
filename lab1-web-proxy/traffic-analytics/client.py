import grpc
import traffic_pb2
import traffic_pb2_grpc


def receive_data():
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = traffic_pb2_grpc.TrafficAnalyzerStub(channel)
        request = traffic_pb2.TrafficData(
            intersection_id=5,
            signal_status_1=9,
            vehicle_count=50,
            incident=False,
            date="10.10.2023",
            time="19:11"
        )
        response = stub.ReceiveData(request)
        print(response.message)

# import grpc
# from grpc import RpcError
# from datetime import datetime, timedelta
#
#
# def receive_data():
#     try:
#         # Create an insecure gRPC channel to the server
#         with grpc.insecure_channel('localhost:8080') as channel:
#             stub = traffic_pb2_grpc.TrafficAnalyzerStub(channel)
#
#             # Create a request with intentionally slow processing
#             request = traffic_pb2.TrafficData(
#                 intersection_id=5,
#                 signal_status_1=9,
#                 vehicle_count=50,
#                 incident=False,
#                 date="07.10.2023",
#                 time="19:11"
#             )
#
#             # Set a deadline for the gRPC call
#             # This sets the deadline to 1 second from the current time
#             deadline = datetime.now() + timedelta(seconds=1)
#
#             # Create a context with the deadline
#             context = grpc.with_deadline(deadline)
#
#             response = stub.ReceiveData(request, context=context)
#             print(response.message)
#
#     except RpcError as e:
#         if e.code() == grpc.StatusCode.DEADLINE_EXCEEDED:
#             print("Request timed out")
#         else:
#             print(f"RPC error: {e.code()} - {e.details()}")
#
#
# if __name__ == '__main__':
#     receive_data()


def get_today_statistics(intersection_id):
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = traffic_pb2_grpc.TrafficAnalyzerStub(channel)
        request = traffic_pb2.IntersectionRequest(intersection_id=intersection_id)
        response = stub.GetTodayStatistics(request)
        print("Today's statistics: ")
        print("Intersection id:", response.intersection_id)
        print("Timestamp:", response.timestamp)
        print("Average vehicle count:", response.average_vehicle_count)
        print("Peak Hours:", response.peak_hours)
        print("Average incidents:", response.average_incidents)


def get_last_week_statistics(intersection_id):
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = traffic_pb2_grpc.TrafficAnalyzerStub(channel)
        request = traffic_pb2.IntersectionRequest(intersection_id=intersection_id)
        response = stub.GetLastWeekStatistics(request)
        print("Last week's statistics: ")
        print("Intersection id:", response.intersection_id)
        print("Timestamp:", response.timestamp)
        print("Average vehicle count:", response.average_vehicle_count)
        print("Peak hours:", response.peak_hours)
        print("Incidents:", response.average_incidents)


def get_next_week_predictions(intersection_id):
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = traffic_pb2_grpc.TrafficAnalyzerStub(channel)
        request = traffic_pb2.IntersectionRequest(intersection_id=intersection_id)
        response = stub.GetNextWeekPredictions(request)
        print("Next week's predictions: ")
        print("Intersection id:", response.intersection_id)
        print("Timestamp:", response.timestamp)
        print("Average vehicle count:", response.average_vehicle_count)
        print("Peak hours:", response.peak_hours)
        print("Incidents:", response.average_incidents)


if __name__ == '__main__':
    receive_data()
    # get_today_statistics(5)
    # get_last_week_statistics(5)
    # get_next_week_predictions(5)
