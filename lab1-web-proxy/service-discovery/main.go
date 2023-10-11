package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"sync"
)

type Service struct {
	Name string `json:"name"`
	Host string `json:"host"`
	Port int    `json:"port"`
}

var (
	servicesMu sync.Mutex
	services   = make(map[string]Service)
)

func registerService(w http.ResponseWriter, r *http.Request) {
	var service Service
	if err := json.NewDecoder(r.Body).Decode(&service); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	servicesMu.Lock()

	if existingService, found := services[service.Name]; found {
		fmt.Printf("Replacing existing service: %s at %s:%d with %s:%d\n", existingService.Name, existingService.Host, existingService.Port, service.Host, service.Port)
	}

	services[service.Name] = service
	servicesMu.Unlock()

	fmt.Printf("Registered service: %s at %s:%d\n", service.Name, service.Host, service.Port)
	w.WriteHeader(http.StatusCreated)
}

func getService(w http.ResponseWriter, r *http.Request) {
	serviceName := r.URL.Query().Get("name")

	servicesMu.Lock()
	service, found := services[serviceName]
	servicesMu.Unlock()

	if !found {
		http.NotFound(w, r)
		return
	}

	err := json.NewEncoder(w).Encode(service)
	if err != nil {
		return
	}
}

func main() {
	http.HandleFunc("/register_service", registerService)
	http.HandleFunc("/get_service_data", getService)

	fmt.Println("Service discovery listening on port 9090...")
	log.Fatal(http.ListenAndServe(":9090", nil))
}
