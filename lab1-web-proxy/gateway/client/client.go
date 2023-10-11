package main

import (
	"context"
	"fmt"
	pb "gateway/gen/traffic_regulation"
	"google.golang.org/grpc"
	"log"
)

func main() {
	conn, err := grpc.Dial("localhost:8081", grpc.WithInsecure())
	if err != nil {
		log.Fatal(err)
	}
	defer func(conn *grpc.ClientConn) {
		err := conn.Close()
		if err != nil {
		}
	}(conn)

	client := pb.NewTrafficRegulationClient(conn)

	request := &pb.TrafficDataForLogs{
		IntersectionId: 1,
		SignalStatus_1: 2,
		VehicleCount:   100,
		Incident:       false,
		Date:           "2023-10-11",
		Time:           "12:00:00",
	}

	resp, err := client.ReceiveDataForLogs(context.Background(), request)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Received response:")
	fmt.Println(resp)
	fmt.Println("Response message:", resp.Message)
}
