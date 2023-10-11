import grpc
import traffic_regulation_pb2
import traffic_regulation_pb2_grpc


def receive_data_for_logs():
    with grpc.insecure_channel('localhost:8081') as channel:
        stub = traffic_regulation_pb2_grpc.TrafficRegulationStub(channel)
        request = traffic_regulation_pb2.TrafficDataForLogs(
            intersection_id=5,
            signal_status_1=9,
            vehicle_count=50,
            incident=False,
            date="10.10.2023",
            time="19:11"
        )
        response = stub.ReceiveDataForLogs(request)
        print(response.message)


if __name__ == '__main__':
    receive_data_for_logs()
