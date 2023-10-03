package main

import (
	"context"
	pb "gateway/gen/proto"
	"github.com/grpc-ecosystem/grpc-gateway/v2/runtime"
	"google.golang.org/grpc"
	"log"
	"net"
	"net/http"
)

type testApiServer struct {
	pb.UnimplementedTestApiServer
}

func (s *testApiServer) Echo(ctx context.Context, req *pb.ResponseRequest) (*pb.ResponseRequest, error) {
	return req, nil
}

func (s *testApiServer) GetUser(ctx context.Context, req *pb.UserRequest) (*pb.UserResponse, error) {
	return &pb.UserResponse{}, nil
}

func main() {
	go func() {
		// multiplexer
		mux := runtime.NewServeMux()

		// register
		err := pb.RegisterTestApiHandlerServer(context.Background(), mux, &testApiServer{})
		if err != nil {
			log.Println(err)
		}

		// http server
		log.Fatalln(http.ListenAndServe("localhost:8081", mux))
	}()

	listen, err := net.Listen("tcp", "localhost:8080")
	if err != nil {
		log.Fatalln(err)
	}

	grpcServer := grpc.NewServer()

	pb.RegisterTestApiServer(grpcServer, &testApiServer{})

	err = grpcServer.Serve(listen)
	if err != nil {
		log.Println(err)
	}
}
