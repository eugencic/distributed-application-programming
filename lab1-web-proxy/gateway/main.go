package main

import (
	"bytes"
	"context"
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"log"
	"net/http"

	pb "gateway/gen"
	"github.com/golang/glog"
	"github.com/grpc-ecosystem/grpc-gateway/v2/runtime"
	"google.golang.org/grpc"
)

type Service struct {
	Name string `json:"name"`
	Host string `json:"host"`
	Port int    `json:"port"`
}

var (
	gatewayName                = "gateway"
	gatewayHost                = "localhost"
	gatewayPort                = 4000
	serviceDiscoveryEndpoint   = "http://localhost:9000"
	trafficAnalyzerServiceName = "traffic-analyzer"
)

func registerWithServiceDiscovery() {
	serviceInfo := Service{
		Name: gatewayName,
		Host: gatewayHost,
		Port: gatewayPort,
	}

	data, err := json.Marshal(serviceInfo)
	if err != nil {
		log.Fatalf("Failed to convert service information in JSON format: %v", err)
	}

	resp, err := http.Post(serviceDiscoveryEndpoint+"/register_service", "application/json", bytes.NewReader(data))
	if err != nil {
		log.Fatalf("Failed to register the gateway with service discovery: %v", err)
	}

	defer func(Body io.ReadCloser) {
		err := Body.Close()
		if err != nil {
		}
	}(resp.Body)

	if resp.StatusCode != http.StatusCreated {
		log.Fatalf("Failed to register the gateway with service discovery: HTTP %d", resp.StatusCode)
	}

	fmt.Printf("%s registered with service discovery\n", gatewayName)
}

func getServiceInfo(serviceName string) (string, int, error) {
	resp, err := http.Get(serviceDiscoveryEndpoint + "/get_service_data?name=" + serviceName)
	if err != nil {
		return "", 0, err
	}

	defer func(Body io.ReadCloser) {
		err := Body.Close()
		if err != nil {
		}
	}(resp.Body)

	if resp.StatusCode != http.StatusOK {
		return "", 0, fmt.Errorf("service not found")
	}

	var service Service
	if err := json.NewDecoder(resp.Body).Decode(&service); err != nil {
		return "", 0, err
	}

	return service.Host, service.Port, nil
}

func run() error {
	ctx := context.Background()
	ctx, cancel := context.WithCancel(ctx)
	defer cancel()

	trafficAnalyzerHost, trafficAnalyzerPort, err := getServiceInfo(trafficAnalyzerServiceName)
	if err != nil {
		log.Fatalf("Failed to retrieve information about the traffic analyzer service: %v", err)
	}

	trafficAnalyzerServerEndpoint := flag.String("traffic-analyzer-server-endpoint", fmt.Sprintf("%s:%d", trafficAnalyzerHost, trafficAnalyzerPort), "traffic analyzer server endpoint")

	flag.Parse()

	grpcMux := runtime.NewServeMux()

	opts := []grpc.DialOption{grpc.WithInsecure()}

	err = pb.RegisterTrafficAnalyzerHandlerFromEndpoint(ctx, grpcMux, *trafficAnalyzerServerEndpoint, opts)
	if err != nil {
		log.Fatalln("Cannot register handler server.")
	}

	mux := http.NewServeMux()

	mux.Handle("/", grpcMux)

	fmt.Println("Gateway listening on port 4000...")

	return http.ListenAndServe(":4000", grpcMux)
}

func main() {

	flag.Parse()
	defer glog.Flush()

	registerWithServiceDiscovery()

	if err := run(); err != nil {
		glog.Fatal(err)
	}
}
