import traffic_pb2
import traffic_pb2_grpc
import grpc
import time


def run():
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = traffic_pb2_grpc.TrafficAnalyzerStub(channel)
        request = traffic_pb2.TrafficData(intersection_id=5, signal_status_1=1)
        response = stub.ReceiveData(request)
        print("Received: ")
        print(response)


if __name__ == '__main__':
    run()
