import grpc
from concurrent import futures
from flask import Flask, request, jsonify, Response
import threading
import traffic_analytics_pb2
import traffic_analytics_pb2_grpc
import traffic_regulation_pb2
import traffic_regulation_pb2_grpc

app = Flask(__name__)

# TRAFFIC_ANALYTICS_SERVICE_ADDRESS = "traffic-analytics-service:7000"
# TRAFFIC_REGULATION_SERVICE_ADDRESS = "traffic-regulation-service:8000"

TRAFFIC_ANALYTICS_SERVICE_ADDRESS = "localhost:7071"
TRAFFIC_REGULATION_SERVICE_ADDRESS = "localhost:8081"


def async_health_check_grpc(service_address):
    def _make_request():
        channel = grpc.insecure_channel(service_address)
        try:
            grpc.channel_ready_future(channel).result(timeout=1)
            print(f"Health check for {service_address} successful.")
        except Exception as e:
            print(f"Health check for {service_address} failed: {str(e)}")

    thread = threading.Thread(target=_make_request)
    thread.start()


def add_traffic_data_analytics(intersection_id, message):
    try:
        channel = grpc.insecure_channel(TRAFFIC_ANALYTICS_SERVICE_ADDRESS)
        stub = traffic_analytics_pb2_grpc.TrafficAnalyticsStub(channel)
        request = traffic_analytics_pb2.AddDataAnalyticsRequest(
            intersection_id=intersection_id,
            message=message,
        )
        response = stub.AddDataAnalytics(request)
        return response
    except grpc.RpcError as e:
        print("Error in add_traffic_data_analytics:")
        import traceback
        traceback.print_exc()
        return e



def add_traffic_data_regulation(intersection_id, message):
    try:
        channel = grpc.insecure_channel(TRAFFIC_REGULATION_SERVICE_ADDRESS)
        stub = traffic_regulation_pb2_grpc.TrafficRegulationStub(channel)
        request = traffic_regulation_pb2.AddDataRegulationRequest(
            intersection_id=intersection_id,
            message=message,
        )
        response = stub.AddDataRegulation(request)
        return response
    except grpc.RpcError as e:
        print("Error in add_traffic_data_regulation:")
        import traceback
        traceback.print_exc()
        return e



def undo_traffic_data_analytics(intersection_id):
    channel = grpc.insecure_channel(TRAFFIC_ANALYTICS_SERVICE_ADDRESS)
    stub = traffic_analytics_pb2_grpc.TrafficAnalyticsStub(channel)
    request = traffic_analytics_pb2.DeleteDataAnalyticsRequest(
        intersection_id=intersection_id,
    )
    response = stub.DeleteDataAnalytics(request)
    print("Undo analytics:")
    print(response)
    return response



def undo_traffic_data_regulation(intersection_id):
    channel = grpc.insecure_channel(TRAFFIC_REGULATION_SERVICE_ADDRESS)
    stub = traffic_regulation_pb2_grpc.TrafficRegulationStub(channel)
    request = traffic_regulation_pb2.DeleteDataRegulationRequest(
        intersection_id=intersection_id,
    )
    response = stub.DeleteDataRegulation(request)
    print("Undo regulation:")
    print(response)
    return response


@app.route('/coordinator/add_data', methods=['POST'])
def add_data():
    try:
        data = request.json
        intersection_id = data.get('intersection_id')
        message = data.get('message')

        # Step 1: Asynchronous health checks
        thread_analytics = threading.Thread(target=lambda: async_health_check_grpc(TRAFFIC_ANALYTICS_SERVICE_ADDRESS))
        thread_regulation = threading.Thread(target=lambda: async_health_check_grpc(TRAFFIC_REGULATION_SERVICE_ADDRESS))
        thread_analytics.start()
        thread_regulation.start()
        # Step 2: Synchronous requests to save data
        response_analytics = add_traffic_data_analytics(intersection_id, message)
        response_regulations = add_traffic_data_regulation(intersection_id, message)
        print("Response analytics:")
        print(response_analytics)
        print("Response regulations:")
        print(response_regulations)
        thread_analytics.join()
        thread_regulation.join()
        # Check if any health check failed
        if isinstance(response_analytics, grpc.RpcError) or isinstance(response_regulations, grpc.RpcError):
            # Undo changes by sending undo requests to both services
            undo_analytics = undo_traffic_data_analytics(intersection_id)
            undo_regulation = undo_traffic_data_regulation(intersection_id)

            # Print responses for both services
            print("Undo analytics:")
            print(undo_analytics)
            print("Undo regulations:")
            print(undo_regulation)
            return jsonify({"status": "error", "message": "Connection health check failed. Changes undone."}), 500

        return jsonify({"status": "success", "message": "Data added successfully."})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6061, debug=True)
