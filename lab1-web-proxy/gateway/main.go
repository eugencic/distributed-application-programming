package main

import (
	"bytes"
	"context"
	"encoding/json"
	"flag"
	"fmt"
	ta "gateway/gen/traffic_analytics"
	tr "gateway/gen/traffic_regulation"
	"github.com/golang/glog"
	"github.com/grpc-ecosystem/grpc-gateway/v2/runtime"
	"google.golang.org/grpc"
	"io"
	"log"
	"net/http"
)

type Service struct {
	Name string `json:"name"`
	Host string `json:"host"`
	Port int    `json:"port"`
}

var (
	gatewayName                  = "Gateway"
	gatewayHost                  = "localhost"
	gatewayPort                  = 4040
	serviceDiscoveryEndpoint     = "http://localhost:9090"
	trafficAnalyticsServiceName  = "traffic-analytics-service"
	trafficRegulationServiceName = "traffic-regulation-service"
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

	trafficAnalyticsHost, trafficAnalyticsPort, err := getServiceInfo(trafficAnalyticsServiceName)
	if err != nil {
		log.Fatalf("Failed to retrieve information about the traffic analytics service: %v", err)
	}

	trafficRegulationHost, trafficRegulationPort, err := getServiceInfo(trafficRegulationServiceName)
	if err != nil {
		log.Fatalf("Failed to retrieve information about the traffic regulation service: %v", err)
	}

	trafficAnalyticsServiceEndpoint := flag.String("traffic-analytics-service-endpoint", fmt.Sprintf("%s:%d", trafficAnalyticsHost, trafficAnalyticsPort), "traffic analytics service endpoint")
	trafficRegulationServiceEndpoint := flag.String("traffic-regulation-service-endpoint", fmt.Sprintf("%s:%d", trafficRegulationHost, trafficRegulationPort), "traffic regulation service endpoint")

	flag.Parse()

	grpcMux := runtime.NewServeMux()

	opts := []grpc.DialOption{grpc.WithInsecure()}

	err = ta.RegisterTrafficAnalyticsHandlerFromEndpoint(ctx, grpcMux, *trafficAnalyticsServiceEndpoint, opts)
	if err != nil {
		log.Fatalln("Cannot register traffic analytics handler server.")
	} else {
		fmt.Println("Traffic analytics service registered.")
	}

	err = tr.RegisterTrafficRegulationHandlerFromEndpoint(ctx, grpcMux, *trafficRegulationServiceEndpoint, opts)
	if err != nil {
		log.Fatalln("Cannot register traffic regulation handler server.")
	} else {
		fmt.Println("Traffic regulation service registered.")
	}

	mux := http.NewServeMux()

	mux.Handle("/", grpcMux)

	fmt.Println("Gateway listening on port 4040...")

	return http.ListenAndServe(":4040", grpcMux)
}

func main() {

	flag.Parse()
	defer glog.Flush()

	registerWithServiceDiscovery()

	if err := run(); err != nil {
		glog.Fatal(err)
	}
}
