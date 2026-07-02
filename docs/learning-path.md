1. Python setup and minimal app

Initialized the project and Git repository.
Planned the project folder structure.
Set up a Python virtual environment.
Installed FastAPI and Uvicorn.
Created requirements.txt.
Built the first FastAPI application.
Learned how uvicorn app.main:app --reload works.
Used FastAPI's automatic Swagger documentation.
Started documenting our learning in docs/03-python.md.

2.  Improved interview-quality explanations for:
    FastAPI() application instance
    requirements.txt
    --reload
    Introduced the Separation of Concerns principle.
    Designed a production-ready FastAPI folder structure.
    Learned the purpose of:
    routers/
    services/
    schemas/
    database/
    config/
    utils/
    Understood why **init**.py exists.
    Added a professional /health endpoint.
    Connected the idea of /health with Kubernetes self-healing.

3.

Correct separation of responsibilities:
.env stores secrets and environment-specific values.
config/settings.py loads and exposes configuration to the application.
Installed python-dotenv.
Created the first .env file.
Built a configuration layer (settings.py).
Updated main.py to use configuration instead of hardcoded values.
Created a proper .gitignore.
Learned why committing secrets to Git is dangerous.
Introduced the best practice of using .env.example.

4.

Mini Summary (Current Chat)
✅ What We Learned
Understood the difference between a Database and a DBMS.
Learned why PostgreSQL is chosen for production applications.
Installed:
sqlalchemy
psycopg2-binary
Updated the .env configuration with database details.
Created the database connection layer (database.py).
Learned the purpose of:
create_engine()
SessionLocal
Base
Built our first ORM model: Task.

5.

Why database schema changes should be handled with migrations (later using Alembic).
Why each request gets its own database session.
Introduced the complete request flow:
Router → Schema → Service → Database
Created the first request schema (TaskCreate).
Built the first business logic function (create_task).
Started the router layer.
Learned the purpose of:
db.add()
db.commit()
db.refresh()
Introduced the Single Responsibility Principle (SRP).

6. Completed Backend CRUD Operations for Task

- Updated `schemas/task.py` to include comprehensive Pydantic models: `TaskBase`, `TaskCreate`, `TaskUpdate`, and `TaskOut`.
- Implemented full CRUD logic in `routers/task_router.py` (GET all, GET by ID, POST, PUT, DELETE).
- Included the `task_router` into the main application via `app.include_router()`.
- Added step-by-step explanatory comments in the router detailing the flow of each HTTP request, from parameter extraction to database session handling, execution, and returning the result.

7.

What We Learned
Why Docker was created ("Works on My Machine" problem).
Difference between Virtual Machines and Containers.
Docker architecture:
Docker Hub
Docker Engine
Image
Container
Difference between an Image (blueprint) and a Container (running instance).
The Docker lifecycle:

8.  Reviewed Image vs Container with interview-quality explanations.
    Learned what a Dockerfile is.
    Understood every instruction:
    FROM
    WORKDIR
    COPY
    RUN
    CMD
    Learned the concept of Docker Layers.
    Understood Docker Layer Caching and why instruction order matters.
    Built our first Docker image using:

9.

Reviewed Docker layer caching with interview-quality explanations.
Understood what docker run actually does internally.
Learned Port Mapping (HOST_PORT:CONTAINER_PORT).
Understood why Uvicorn must listen on 0.0.0.0.
Learned:
docker ps
docker ps -a
docker logs
docker exec
docker stop
docker start
docker rm
Learned the complete Docker container lifecycle.
Introduced the purpose of .dockerignore.

10. Why localhost doesn't work between containers.
    How Docker Compose manages multiple services.
    Built a compose.yaml with:
    Backend service
    PostgreSQL service
    Learned:
    build
    image
    ports
    depends_on
    environment
    Understood Docker's internal DNS using service names.
    Introduced Docker Volumes for persistent database storage.
    Learned:
    docker compose up
    docker compose up -d
    docker compose down

11. Why a working Docker image isn't always production-ready.
    Created and understood the purpose of .dockerignore.
    Learned about Docker Build Context.
    Understood how .dockerignore improves:
    Build speed
    Image cleanliness
    Security
    Introduced Multi-Stage Builds and why they're useful.
    Learned the concept of Health Checks.
    Connected today's learning with future Kubernetes concepts.

12.

Reviewed why .env and .venv should not be included in Docker images.
Introduced Continuous Integration (CI).
Learned what GitHub Actions is and why it's used.
Created our first workflow:
Trigger on push.
Checkout code.
Set up Python.
Install dependencies.
Verify Docker.
Compile Python code.
Understood that GitHub Actions runs on a fresh Ubuntu VM for every workflow.

13. Reviewed how CI stops immediately when a critical step fails.
    Fixed another GitHub Actions typo (compileeall → compileall).
    Learned how compileall catches Python syntax errors.
    Introduced Docker Hub as a container registry.
    Planned a CI pipeline that:
    Logs in securely.
    Builds the Docker image.
    Pushes versioned images automatically.

14.

Reviewed how CI stops immediately when a critical step fails.
Fixed another GitHub Actions typo (compileeall → compileall).
Learned how compileall catches Python syntax errors.
Introduced Docker Hub as a container registry.
Planned a CI pipeline that:
Logs in securely.
Builds the Docker image.
Pushes versioned images automatically.

15.

Understood how SSH communicates with a remote EC2 server.
Configured PuTTY to use an AWS key pair.
Learned essential Linux commands:
pwd
whoami
hostname
uname -a
ls
Learned the purpose of apt update vs apt upgrade.
Prepared the server for Docker installation.

16. Installed Docker from Docker's official repository.
    Understood the purpose of GPG keys and package repositories.
    Installed:
    Docker Engine
    Docker CLI
    Docker Compose Plugin
    Buildx
    Configured Docker for the ubuntu user.
    Ran the first container using hello-world.

17.

Reviewed Linux group permissions and why reconnecting after usermod is necessary.
Understood that production servers pull prebuilt Docker images instead of rebuilding them.
Prepared the deployment structure for EC2.
Learned how to:
Pull images from Docker Hub.
Start containers with Docker Compose.
Verify deployments.
Use logs for troubleshooting.

18.

Reviewed Linux group permissions and why reconnecting after usermod is necessary.
Understood that production servers pull prebuilt Docker images instead of rebuilding them.
Prepared the deployment structure for EC2.
Learned how to:
Pull images from Docker Hub.
Start containers with Docker Compose.
Verify deployments.
Use logs for troubleshooting.

19. Your EC2 instance running.
    docker ps showing the backend and PostgreSQL containers.
    curl localhost:8000 returning your API response.

20.

What We Decided
We do not need to buy a domain right now.
We'll continue learning using your EC2 public IP.
HTTPS with Let's Encrypt will come later when you have a domain.
We'll prioritize real DevOps skills over spending money.

21.

Introduced Nginx as a reverse proxy.
Containerized Nginx instead of installing it directly on Ubuntu.
Created an nginx.conf to forward requests to the FastAPI service.
Updated compose.yaml to include an Nginx container.
Learned how Docker's internal DNS lets containers communicate using service names like backend.

22.

Why a single backend eventually becomes a bottleneck.
How Nginx distributes traffic across multiple backend instances.
The idea of Docker Compose scaling.
Common load-balancing algorithms:
Round Robin
Least Connections
IP Hash
Why horizontal scaling improves both performance and availability

23.

Introduced Prometheus as a metrics collector.
Introduced Grafana as a visualization platform.
Understood the difference between metrics and logs.
Added Prometheus and Grafana to our Docker Compose architecture.
Learned why exporters are needed to collect real system metrics.

24. curl localhost:9090 works, so Prometheus is running correctly.
    The issue is most likely outside the container (AWS networking or campus firewall).
    We have a structured debugging plan:
    Check Docker port mapping.
    Verify the EC2 Security Group.
    Test from a different network (mobile hotspot).
    Confirm external reachability.

25.

Your EC2 deployment is healthy.
Prometheus is reachable from outside the server.
The issue is specific to your college Wi-Fi, not your application or AWS setup.
Rather than exposing multiple ports, we'll route everything through Nginx on port 80, which is also the more production-oriented design.

26. Added Prometheus container.

Configured:

prometheus.yml

Created scrape jobs.

Initially monitored:

Prometheus itself
💡 Learned
Metrics
Scraping
Time-series database
Prometheus architecture

Added Grafana.

Opened:

http://EC2_PUBLIC_IP:3000

Connected Prometheus as the data source.

💡 Learned
Dashboards
Visualization
Data Sources

Added:

prom/node-exporter

Mounted:

/proc
/sys
/

Configured Prometheus:

- job_name: node-exporter

Verified:

node-exporter:9100

Imported:

Node Exporter Full Dashboard.

💡 Learned

Node Exporter exposes:

CPU
Memory
Disk
Network
Filesystem
Linux host metrics

Architecture:

Linux
│
Node Exporter
│
Prometheus
│
Grafana

Added:

gcr.io/cadvisor/cadvisor

Mounted:

Docker runtime
Docker storage
Root filesystem
Kernel information

Configured Prometheus:

- job_name: cadvisor

Imported Docker dashboard.

💡 Learned

cAdvisor monitors:

Container CPU
Container Memory
Network usage
Filesystem usage
Docker container metrics

Architecture:

Docker Containers
│
cAdvisor
│
Prometheus
│
Grafana

                   Linux Host
                       │
        ┌──────────────┴──────────────┐
        │                             │
        ▼                             ▼

Node Exporter cAdvisor
│ │
└──────────────┬──────────────┘
▼
Prometheus
│
▼
Grafana
