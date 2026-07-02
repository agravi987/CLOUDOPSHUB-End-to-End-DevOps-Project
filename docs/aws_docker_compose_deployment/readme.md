🚀 CloudOpsHub DevOps Journey Summary (EC2 → Docker Compose → Monitoring)
🎯 Goal

Deploy the CloudOpsHub FastAPI application to AWS using production-like DevOps practices and build a complete monitoring stack.

Phase 1 — Launch AWS EC2
✅ Created an EC2 Instance
Launched an Ubuntu EC2 instance.
Allowed SSH (22) in the Security Group.
Connected using PuTTY/SSH.

Learned:

Public IP
Security Groups
Key Pair authentication
Phase 2 — Prepare the Server

Updated Ubuntu:

sudo apt update
sudo apt upgrade -y

Installed Docker:

sudo apt install docker.io -y

Enabled Docker:

sudo systemctl enable docker
sudo systemctl start docker

Added the Ubuntu user to the Docker group:

sudo usermod -aG docker ubuntu

Logged out and back in.

Verified:

docker --version
docker ps
💡 Learned
Linux package installation
Docker daemon
Linux user permissions
Why Docker group access is needed
Phase 3 — Deploy Using Docker Hub

Instead of copying source code to the server:

GitHub
↓
GitHub Actions
↓
Docker Hub
↓
EC2

Pulled the prebuilt Docker image from Docker Hub.

💡 Learned
Immutable Docker images
CI builds once, deploy many times
Faster and more reliable deployments
Phase 4 — Docker Compose

Created a production compose.yaml.

Services:

FastAPI Backend
PostgreSQL
Nginx

Later added:

Prometheus
Grafana
Node Exporter
cAdvisor
💡 Learned
Multi-container applications
Docker Compose networking
Service discovery using service names
Persistent Docker volumes
Phase 5 — Environment Variables

Created:

.env

Stored:

Database Host
Port
Username
Password
Database Name

Never stored secrets inside Docker images.

💡 Learned
Twelve-Factor App principles
Configuration outside the application
Secure secret management basics
Phase 6 — Reverse Proxy with Nginx

Configured Nginx.

Flow:

Internet
│
▼
Nginx (Port 80)
│
▼
FastAPI

Configured:

proxy_pass
Forwarded headers
Host forwarding
💡 Learned
Reverse Proxy
Single entry point
Why production apps rarely expose application ports directly
Phase 7 — Deploy the Application

Started everything:

docker compose up -d

Verified:

docker ps

Checked:

http://EC2_PUBLIC_IP/

Swagger:

http://EC2_PUBLIC_IP/docs
💡 Learned
Container lifecycle
Port mapping
Production deployment
Phase 8 — Prometheus

Added Prometheus container.

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
Phase 9 — Grafana

Added Grafana.

Opened:

http://EC2_PUBLIC_IP:3000

Connected Prometheus as the data source.

💡 Learned
Dashboards
Visualization
Data Sources
Phase 10 — Node Exporter

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
Phase 11 — cAdvisor

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
Phase 12 — Monitoring Architecture

Final monitoring flow:

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
Final Docker Compose Architecture
Internet
│
▼
Nginx (80)
│
▼
FastAPI
│
▼
PostgreSQL

Prometheus (9090)

Grafana (3000)

Node Exporter (9100)

cAdvisor (8080)
