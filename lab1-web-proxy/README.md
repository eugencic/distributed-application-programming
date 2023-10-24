# Laboratory work Nr.1: Web Proxy 

## Intelligent Traffic Lights Control and Analytics System

> **Performed by:** Eugeniu Popa, FAF-202 \
> **Verified by:** univ. asist. Maxim Voloșenco

### 1. Assess Application Suitability

Here is why this application is relevant for microservices and why distributed systems are necessary:

- **Complexity and scalability**: the application involves components like traffic regulation, data analysis, user and notification. As the infrastructure grows, the system becomes more complex. Microservices are well-suited for handling such complexity by breaking it down into smaller, manageable components, which can be individually scaled to meet varying demands. **Facebook**, for instance, manages a complex system with features like the news feed, messaging, and user profiles through microservices.
- **Independent development**: different aspects of the application, such as regulation and analytics, can be developed and updated independently by separate teams. This allows faster development cycles. For example, the team working on data analysis can add new functionallities without affecting the traffic regulation service. Companies like **Netflix**, with its streaming platform, build and deploy microservices independently, enabling rapid feature development.
- **Fault Isolation**: if one component fails, it doesn't necessarily bring down the entire system. For example, the traffic regulation service would continue to work, even if the analytics service has problems. **Facebook**'s Messenger service is a great example. Even if the Messenger service experiences issues, the main Facebook platform can continue to operate.
- **Technology diversity**: microservices provide the flexibility to select the most suitable technology stack or database for each individual component of the application, acknowledging that different parts of the system may have distinct requirements. **Airbnb** utilizes multiple programming languages and frameworks across its microservices to optimize performance and development efficiency.
- **Easier maintenance**: managing maintenance tasks becomes more convenient when focusing on individual services. This allows making updates, or troubleshooting in a single service without causing disruptions to the entire application.

### 2. Define Service Boundaries

The application's architecture will be organized in the following manner, with the service boundaries described below:

- **Traffic regulation microservice:**
    It is the operational heart of the system, tasked with traffic regulation. Its primary responsibilities include:
    - Monitoring traffic conditions using data from an external source.
    - Implementing traffic control logic to optimize traffic flow.
    - Communicating with traffic lights.
    - Logging traffic signal events and control decisions.
    
- **Traffic analytics microservice:**
    It focuses on analyzing traffic data to provide valuable insights and historical reports. Its primary responsibilities include:
    - Processing and aggregating data from an external source.
    - Storing historical traffic and traffic lights signal events data and analytics results.

System architecture diagram:
![Diagram](https://github.com/eugencic/distributed-application-programming/blob/main/lab1-web-proxy/docs/diagrams/system_architecture_diagram.jpg)


### 3. Choose Technology Stack and Communication Patterns:

- Gateway and service discovery: `Go` programming language
- Microservices: `Python` programming language
- Databases: `PostgreSQL`
- Communication pattern: `RPC`, `REST API`

### 4. Design Data Management:

  - Gateway endpoint and request to traffic control microservice (receiving traffic data):
   `Endpoint`: gateway/traffic-control/receive-data
    ```
    POST /traffic-control-microservice/receive-data
    {
      "intersection_id": "1",
      "timestamp": "2023-09-27T10:15:00Z",
      "signal_status_1": "green",
      "vehicle_count": 35,
      "incident": false
    }
    ```
    
  - Traffic control microservice response (receiving traffic data):
    ```
    {
        "message": "Traffic data received successfully.",
        "timestamp": "2023-09-26T10:17:30Z"
    }
    ```
    
  - Gateway request to traffic control microservice (retrieving traffic lights command logs for daily periods):
    `Endpoint`: gateway/traffic-control/traffic-light-control-logs/daily
    ```
    POST /traffic-control-microservice/traffic-light-control-logs/daily
    {
        "intersection_id": "1",
        "date": "2023-09-26"
    }
    ```

  - Traffic control microservice response (retrieving traffic lights command logs for daily periods):
    ```
    {
      "intersection_id": "1",
      "date": "2023-09-26",
      "logs": [
            {
              "timestamp": "2023-09-26T08:15:00Z",
              "event": "Control Command Sent",
              "description": "Command: North-South: Green, East-West: Red"
            },
            {
              "timestamp": "2023-09-26T09:30:00Z",
              "event": "Control Command Sent",
              "description": "Command: North-South: Red, East-West: Green"
            },
            {
              "timestamp": "2023-09-26T12:45:00Z",
              "event": "Control Command Sent",
              "description": "Command: North-South: Green, East-West: Red"
            },
            {
              "timestamp": "2023-09-26T16:20:00Z",
              "event": "Control Command Sent",
              "description": "Command: North-South: Red, East-West: Green"
            }
        ]
    }
    ```

  - Gateway request to traffic control microservice (retrieving traffic lights command logs for weekly periods):
    `Endpoint`: gateway/traffic-control/traffic-light-control-logs/weekly
    ```
    POST /traffic-control-microservice/traffic-light-control-logs/weekly
    {
      "intersection_id": "1",
      "start_date": "2023-09-19",
      "end_date": "2023-09-26"
    }
    ```
    
 - Traffic control microservice response (retrieving traffic lights command logs for weekly periods):
    ```
    {
      "intersection_id": "1",
      "start_date": "2023-09-19",
      "end_date": "2023-09-26",
      "logs": [
            {
              "timestamp": "2023-09-20T09:45:00Z",
              "event": "Control Command Sent",
              "description": "Command: North-South: Green, East-West: Red"
            },
            {
              "timestamp": "2023-09-22T11:10:00Z",
              "event": "Control Command Sent",
              "description": "Command: North-South: Red, East-West: Green"
            },
            {
              "timestamp": "2023-09-25T14:30:00Z",
              "event": "Control Command Sent",
              "description": "Command: North-South: Green, East-West: Red"
            },
            {
              "timestamp": "2023-09-25T16:50:00Z",
              "event": "Control Command Sent",
              "description": "Command: North-South: Red, East-West: Green"
            }
        ]
    }
    ```

 - Gateway endpoint and request to analytics microservice (receiving traffic data for analysis):
    `Endpoint`: gateway/analytics/receive-data
    ```
    POST /analytics-microservice/receive-data
    {
        "intersection_id": "1",
        "timestamp": "2023-09-27T10:15:00Z",
        "signal_status_1": "green",
        "vehicle_count": 35,
        "incident": false
    }
    ```
    
 - Analytics microservice response (receiving traffic data for analysis):
    ```
    {
      "message": "Traffic data received and processed for analysis.",
      "timestamp": "2023-09-27T10:18:30Z"
    }
    ```

 - Gateway endpoint and request to analytics microservice (retrieving today's traffic analytics for a specific intersection):
    `Endpoint`: gateway/analytics/traffic-analytics/today
    ```
    POST /analytics-microservice/traffic-analytics/today
    {
      "intersection_id": "1",
      "user_id": "12345"
    }
    ```

 - Analytics microservice response (retrieving today's traffic analytics for a specific intersection):
    ```
    {
      "intersection_id": "1",
      "user_id": "12345",
      "timestamp": "2023-09-27T10:20:00Z",
      "analytics_data": {
        "average_vehicle_count": 45,
        "traffic_density": "Moderate",
        "peak_hours": [
          "07:00 AM - 09:00 AM",
          "05:00 PM - 07:00 PM"
        ],
        "incidents": 1,
            "traffic_light_analytics": {
            "average_green_duration": "45 seconds",
            "average_red_duration": "30 seconds",
            "most_frequent_green_timing": "Morning peak hours",
            "most_frequent_red_timing": "Afternoon rush hours",
            "signal_timing_variability": "Low"
        }
      }
    }
    ```

 - Gateway endpoint and request to analytics microservice (retrieving past week's traffic analytics for a specific intersection):
  `Endpoint`: POST /analytics-microservice/traffic-analytics/past-week
    ```
    POST /analytics-microservice/traffic-analytics/past-week
    {
      "intersection_id": "1",
      "user_id": "12345"
    }
    ```

 - Analytics microservice response (retrieving past week's traffic analytics for a specific intersection):
    ```
    {
      "intersection_id": "1",
      "user_id": "12345",
      "timestamp": "2023-09-27T10:22:00Z",
      "analytics_data": {
        "average_vehicle_count": 42,
        "traffic_density": "Moderate",
        "incidents_last_week": 5,
        {
          "average_green_duration": "50 seconds",
          "average_red_duration": "25 seconds",
          "most_frequent_green_timing": "Afternoon rush hours",
          "most_frequent_red_timing": "Late night hours",
          "signal_timing_variability": "High"
        }
      }
    }
    ```

 - Gateway request to analytics microservice (retrieving traffic predictions for the next week for a specific intersection):
  `Endpoint`: gateway/analytics/traffic-predictions/next-week
    ```
    POST /analytics-microservice/traffic-predictions/next-week
    {
      "intersection_id": "1"
    }
    ```

 - Analytics microservice response (retrieving traffic predictions for the next week for a specific intersection):
    ```
    {
      "intersection_id": "1",
      "user_id": "12345",
      "timestamp": "2023-09-27T10:25:00Z",
      "prediction_data": {
        "next_peak_hours": [
          "08:00 AM - 10:00 AM",
          "04:00 PM - 06:00 PM"
        ],
        "traffic_trend": "Stable",
        "estimated_incidents": 2
      }
    }
    ```

 - Gateway request to user microservice (user registrarion):
    `Endpoint`: gateway/user/register
    ```
    POST /user-microservice/register
    {
       "username": "john_doe",
       "password": "password123",
       "role": "user"
    }
    ```
     
 - User microservice response (user registrarion):
     ```
    {
    "message": "User registered successfully."
    }
     ```
     
 - Gateway request to user microservice (user login):
    `Endpoint`: gateway/user/login
    ```
    POST /user-microservice/login
    {
       "username": "john_doe",
       "password": "password123"
    }
     ```
     
  - User microservice response (user login):
     ```
    {
    "user_id": "12345",
    "username": "john_doe",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    }
     ```
     
 - Gateway request to user microservice (user role check):
    `Endpoint`: gateway/user/role
    ```
    POST /user-microservice/role
    {
       "user_id": "12345",
       "password": "password123"
    }
     ```
     
  - User microservice response (user role check):
    ```
    {
    "user_id": "12345",
    "role": "policeman"
    }
    ```

 - Gateway request to notification microservice (add traffic light):
    `Endpoint`: gateway/notification/add-light
    ```
    POST /notification-microservice/add-light
    {
    "user_id": "12345",
    "intersection_id": "1"
    }
    ```

  - Notification microservice response (add traffic light)
    ```
    {
    "message": "Traffic light added for notifications."
    }
    ```

 - Gateway request to notification microservice (remove traffic light):
    `Endpoint`: gateway/notification/remove-light
    ```
    POST /notification-microservice/remove-light
    {
    "user_id": "12345",
    "intersection_id": "1"
    }
    ```

  - Notification microservice response (add traffic light)
    ```
    {
    "message": "Traffic light removed from notifications."
    }
    ```
    
 - Gateway request to notification microservice (get notifications):
    `Endpoint`: gateway/notification/get-notifications
    ```
    POST /notification-microservice/get-notifications
    {
    "user_id": "12345",
    }
    ```

  - Notification microservice response (get notifications)
    ```
    {
    "notifications": [
            {
            "timestamp": "2023-09-27T10:30:00Z",
            "message": "Traffic light at Intersection 1 is currently red."
            },
            {
            "timestamp": "2023-09-27T12:15:00Z",
            "message": "Traffic light at Intersection 2 is currently green."
            }
        ]
    }
    ```

### 5. Set Up Deployment and Scaling:

To ensure modularity and isolation, each microservice in the application will be deployed within its own `Docker` container. For this purpose, individual Dockerfiles will be created for each microservice, containing all the necessary instructions for building the corresponding container image.

To streamline the orchestration of these containers and facilitate the management of the entire application, `Docker Compose` will be employed. Docker Compose simplifies the deployment process by creating and configuring containers, as well as establishing the necessary network connections between them.

