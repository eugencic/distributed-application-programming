# Laboratory work Nr.1: Web Proxy 

## Intelligent Traffic Lights Control and Analytics System

> **Performed by:** Eugeniu Popa, FAF-202 \
> **Verified by:** univ. asist. Maxim Voloșenco

## Run the application

Before running the application, make sure [Docker](https://www.docker.com/) is installed.  
Type this command in the root folder.

```bash
$ docker compose up --build
```

### Application suitability

Here is why this application is relevant for microservices and why distributed systems are necessary:

- **Complexity and scalability**: the application involves components like traffic regulation and data analysis. As the infrastructure grows, the system becomes more complex. Microservices are well-suited for handling such complexity by breaking it down into smaller, manageable components, which can be individually scaled to meet varying demands. **Facebook**, for instance, manages a complex system with features like the news feed, messaging, and user profiles through microservices.
- **Independent development**: different aspects of the application, such as regulation and analytics, can be developed and updated independently by separate teams. This allows faster development cycles. For example, the team working on data analysis can add new functionallities without affecting the traffic regulation service. Companies like **Netflix**, with its streaming platform, build and deploy microservices independently, enabling rapid feature development.
- **Fault Isolation**: if one component fails, it doesn't necessarily bring down the entire system. For example, the traffic regulation service would continue to work, even if the analytics service has problems. **Facebook**'s Messenger service is a great example. Even if the Messenger service experiences issues, the main Facebook platform can continue to operate.
- **Technology diversity**: microservices provide the flexibility to select the most suitable technology stack or database for each individual component of the application, acknowledging that different parts of the system may have distinct requirements. **Airbnb** utilizes multiple programming languages and frameworks across its microservices to optimize performance and development efficiency.
- **Easier maintenance**: managing maintenance tasks becomes more convenient when focusing on individual services. This allows making updates, or troubleshooting in a single service without causing disruptions to the entire application.

### Service boundaries

System architecture diagram:
![Diagram](https://github.com/eugencic/distributed-application-programming/blob/main/lab1-web-proxy/docs/system_architecture_diagram.png)

The application's architecture is organized in the following manner, with the service boundaries described below:

- **Traffic regulation service:**
    It is the operational heart of the system, tasked with traffic regulation. Its primary responsibilities include:
    - Monitoring traffic conditions using data from an external source.
    - Implementing traffic control logic to optimize traffic flow.
    - Communicating with traffic lights.
    - Logging traffic signal events and control decisions.
    
- **Traffic analytics microservice:**
    It focuses on analyzing traffic data to provide valuable insights and historical reports. Its primary responsibilities include:
    - Processing and aggregating data from an external source.
    - Storing historical traffic data and analytics results.

### Technology stack and communication patterns:

- Gateway, service discovery: `Go`
- Traffic analytics and regulation services, load balancers: `Python`
- Databases: `PostgreSQL`
- Communication patterns: `RPC`, `REST`

### Data management:

  - Get status of the gateway:

    ```
    GET http://localhost:6060/get_gateway_status
    ```

  - Get status of the service discovery:

    ```
    GET http://localhost:6060/get_service_discovery_status
    ```

  - Get status of the traffic analytics service:

    ```
    POST http://localhost:6060/get_traffic_analytics_service_status
    ```

  - Send data for analytics:

    ```
    POST http://localhost:6060/receive_data_for_analytics
    {
      "intersection_id": 1,
      "signal_status_1": 1,
      "vehicle_count": 5,
      "incident": true,
      "date": "2023-10-24",
      "time": "07:10"
    }
    ```

  - Get today statistics:

    ```
    POST http://localhost:6060/get_today_statistics
    {
      "intersection_id": 1
    }
    ```

  - Get last week statistics:

    ```
    POST http://localhost:6060/get_last_week_statistics
    {
      "intersection_id": 1
    }
    ```

  - Get next week predictions:

    ```
    POST http://localhost:6060/get_next_week_predictions
    {
      "intersection_id": 1
    }
    ```

  - Get status of the traffic regulation service:

    ```
    POST http://localhost:6060/get_traffic_regulation_service_status
    ```

  - Send data for logs (in order to make logs, signal_status_1 has to be 1 and vehicle_count > 30, or signal_status_1 has to be 2 and vehicle_count < 5):

    ```
    POST http://localhost:6060/receive_data_for_logs 
    {
      "intersection_id": 1,
      "signal_status_1": 1,
      "vehicle_count": 31,
      "incident": true,
      "date": "2023-10-24",
      "time": "07:10"
    }
    ```

  - Get today control logs:

    ```
    POST http://localhost:6060/get_today_control_logs
    {
      "intersection_id": 1
    }
    ```

  - Get last week control logs:

    ```
    POST http://localhost:6060/get_last_week_control_logs
    {
      "intersection_id": 1
    }
    ```

### Deployment and scaling:

To ensure modularity and isolation, each microservice in the application is deployed within its own `Docker` container. For this purpose, individual Dockerfiles are created for each microservice, containing all the necessary instructions for building the corresponding container image.

To streamline the orchestration of these containers and facilitate the management of the entire application, `Docker Compose` is employed. Docker Compose simplifies the deployment process by creating and configuring containers, as well as establishing the necessary network connections between them.
