create:
	protoc --go_out=gen/proto proto/test.proto
	protoc --go-grpc_out=gen/proto/ proto/test.proto
	protoc -I . --grpc-gateway_out ./gen/proto \
		--grpc-gateway_opt logtostderr=true \
		--grpc-gateway_opt paths=source_relative \
		--grpc-gateway_opt generate_unbound_methods=true \
		proto/test.proto

clean:
	rm gen/proto/*.go
