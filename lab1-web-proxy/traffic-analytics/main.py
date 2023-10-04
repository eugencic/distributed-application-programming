from flask import Flask

import traffic_pb2
import traffic_pb2_grpc
import grpc

app = Flask("analytics-service")

from concurrent import futures


class TrafficAnalyzerServicer(traffic_pb2_grpc.TrafficAnalyzerServicer):
    def ReceiveData(self, request, context):
        print("Request: ")
        print(request)
        print("Intersection ")
        print(request.intersection_id)
        response = traffic_pb2.TrafficDataReceiveResponse()
        response.message = f"{request.intersection_id} {request.signal_status_1}"
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    traffic_pb2_grpc.add_TrafficAnalyzerServicer_to_server(TrafficAnalyzerServicer(), server)
    server.add_insecure_port("localhost:8080")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

# @app.route('/')
# def home():
#     return 'Hello, World!'
#
#
# @app.route('/api/analytics/receive-data', methods=['POST', 'GET'])
# def print_data():
#     data = request.get_json()  # Assumes the incoming data is in JSON format
#     if data:
#         print("Received data:", data)
#         return 'Data received and printed!'
#     else:
#         return 'No data received.'
#
#
# if __name__ == '__main__':
#     app.run(port=8080)
