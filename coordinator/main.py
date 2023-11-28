import grpc
from concurrent.futures import ThreadPoolExecutor, wait
from flask import Flask, request, jsonify

import traffic_analytics_pb2
import traffic_analytics_pb2_grpc
import traffic_regulation_pb2
import traffic_regulation_pb2_grpc

app = Flask(__name__)

TRAFFIC_ANALYTICS_SERVICE_ADDRESS = "localhost:7071"
TRAFFIC_REGULATION_SERVICE_ADDRESS = "localhost:8081"


def add_traffic_data_analytics(intersection_id, message):
    channel = grpc.insecure_channel(TRAFFIC_ANALYTICS_SERVICE_ADDRESS)
    stub = traffic_analytics_pb2_grpc.TrafficAnalyticsStub(channel)
    request = traffic_analytics_pb2.AddDataAnalyticsRequest(
        intersection_id=intersection_id,
        message=message,
    )
    response = stub.AddDataAnalytics(request)
    return response


def add_traffic_data_regulation(intersection_id, message):
    channel = grpc.insecure_channel(TRAFFIC_REGULATION_SERVICE_ADDRESS)
    stub = traffic_regulation_pb2_grpc.TrafficRegulationStub(channel)
    request = traffic_regulation_pb2.AddDataRegulationRequest(
        intersection_id=intersection_id,
        message=message,
    )
    response = stub.AddDataRegulation(request)
    return response


def undo_traffic_data_analytics(intersection_id):
    channel = grpc.insecure_channel(TRAFFIC_ANALYTICS_SERVICE_ADDRESS)
    stub = traffic_analytics_pb2_grpc.TrafficAnalyticsStub(channel)
    request = traffic_analytics_pb2.DeleteDataAnalyticsRequest(
        intersection_id=intersection_id,
    )
    response = stub.DeleteDataAnalytics(request)
    return response


def undo_traffic_data_regulation(intersection_id):
    channel = grpc.insecure_channel(TRAFFIC_REGULATION_SERVICE_ADDRESS)
    stub = traffic_regulation_pb2_grpc.TrafficRegulationStub(channel)
    request = traffic_regulation_pb2.DeleteDataRegulationRequest(
        intersection_id=intersection_id,
    )
    response = stub.DeleteDataRegulation(request)
    return response


def saga_coordinator(intersection_id, message):
    try:
        print("Step 1: Add data to Traffic Analytics")
        with ThreadPoolExecutor() as executor:
            future_analytics = executor.submit(add_traffic_data_analytics, intersection_id, message)

        print("Step 2: Add data to Traffic Regulation")
        with ThreadPoolExecutor() as executor:
            future_regulations = executor.submit(add_traffic_data_regulation, intersection_id, message)

        wait([future_analytics, future_regulations])

        print("Steps Completed. Proceeding to compensating actions if needed.")

        future_analytics.result()
        future_regulations.result()

        print("No nee for compensating actions.")

        return 200

    except Exception as e:
        print("Exception during saga coordination:", str(e))
        print("Compensate: Undo changes made by previous steps...")

        with ThreadPoolExecutor() as compensator_executor:
            future_analytics = compensator_executor.submit(undo_traffic_data_analytics, intersection_id)
            future_regulations = compensator_executor.submit(undo_traffic_data_regulation, intersection_id)

            wait([future_analytics, future_regulations])

            print("Compensating actions completed.")

            return 500


@app.route('/add_data', methods=['POST'])
def add_data():
    try:
        data = request.json
        intersection_id = data.get('intersection_id')
        message = data.get('message')

        print("Initiate Saga")
        response = saga_coordinator(intersection_id, message)

        if response == 500:
            return jsonify({"message": "Internal Server Error"}), 500

        return jsonify({"message": "Data added successfully"}), 200

    except Exception as e:
        return jsonify({"message": "Internal Server Error"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6061, debug=True)
