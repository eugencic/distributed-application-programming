package main

import (
	"context"
	"flag"
	"log"
	"net/http"

	pb "gateway/gen"
	"github.com/golang/glog"
	"github.com/grpc-ecosystem/grpc-gateway/v2/runtime"
	"google.golang.org/grpc"
)

var (
	trafficAnalyzerServerEndpoint = flag.String("traffic-analyzer-server-endpoint", "localhost:8080", "traffic analyzer server endpoint")
)

func run() error {
	ctx := context.Background()
	ctx, cancel := context.WithCancel(ctx)
	defer cancel()

	grpcMux := runtime.NewServeMux()

	opts := []grpc.DialOption{grpc.WithInsecure()}

	err := pb.RegisterTrafficAnalyzerHandlerFromEndpoint(ctx, grpcMux, *trafficAnalyzerServerEndpoint, opts)
	if err != nil {
		log.Fatalln("Cannot register handler server.")
	}

	mux := http.NewServeMux()

	mux.Handle("/", grpcMux)

	return http.ListenAndServe(":4040", grpcMux)
}

func main() {

	flag.Parse()
	defer glog.Flush()

	if err := run(); err != nil {
		glog.Fatal(err)
	}
}
