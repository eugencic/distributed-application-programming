create:
	python3 -m grpc_tools.protoc -I proto --python_out=. --grpc_python_out=. --pyi_out=. proto/traffic.proto
clear:
	python3 -m rm traffic_pb2.py
	python3 -m rm traffic_pb2_grpc.py
