# 🌐 Phase 2 — Dockerized Infrastructure & Reverse Proxy Architecture

Phase 2 transformed the Farm Inventory platform into a fully containerized multi-service infrastructure with production-style networking and reverse proxy architecture.

---

# 🎯 Objectives

Phase 2 implemented:

* Full Dockerized deployment
* Multi-container orchestration
* Persistent PostgreSQL storage
* NGINX reverse proxy integration
* Internal container networking
* Local domain routing
* Windows host integration
* Disaster recovery validation

---

# 🏗️ Infrastructure Architecture

```text id="kl4br0"
                    farm-ml.local
                           │
                    ┌────────────┐
                    │   NGINX    │
                    │ Reverse    │
                    │ Proxy      │
                    └─────┬──────┘
                          │
        ┌─────────────────┼─────────────────┐
        ▼                                   ▼
 ┌────────────┐                     ┌────────────┐
 │ Streamlit  │                     │  FastAPI   │
 │ Dashboard  │                     │ Backend API│
 └────────────┘                     └─────┬──────┘
                                          ▼
                                 ┌────────────────┐
                                 │ PostgreSQL DB  │
                                 │ Persistent DB  │
                                 └────────────────┘
```

---

# 🐳 Dockerized Services

The stack currently includes:

| Service    | Purpose                           |
| ---------- | --------------------------------- |
| FastAPI    | Backend APIs and ML inference     |
| Streamlit  | Analytics dashboard frontend      |
| PostgreSQL | Persistent database               |
| NGINX      | Reverse proxy and ingress gateway |

---

# 📂 Container Names

| Container  | Name           |
| ---------- | -------------- |
| FastAPI    | farm_fastapi   |
| Streamlit  | farm_streamlit |
| PostgreSQL | farm_postgres  |
| NGINX      | farm_nginx     |

---

# 🐳 Docker Compose Orchestration

All services are orchestrated using Docker Compose.

---

# 🚀 Start Full Stack

```bash id="v5h4m2"
docker compose up -d --build
```

This automatically:

* builds containers
* creates Docker networks
* starts all services
* initializes infrastructure

---

# 🔍 Verify Running Containers

```bash id="z9e2q8"
docker compose ps
```

Expected containers:

* farm_fastapi
* farm_streamlit
* farm_postgres
* farm_nginx

---

# 🔗 Internal Docker Networking

Services communicate internally using Docker service names.

Example:

| Service    | Internal Hostname |
| ---------- | ----------------- |
| FastAPI    | fastapi           |
| Streamlit  | streamlit         |
| PostgreSQL | postgres          |
| NGINX      | nginx             |

---

# 💾 PostgreSQL Persistence

Persistent storage is enabled using Docker volumes.

```yaml id="cfh0x5"
volumes:
  postgres_data:
```

This ensures:

* database persistence
* recovery after restarts
* operational durability

---

# 🛠️ Database Initialization Inside Container

After starting containers, initialize tables inside the FastAPI container.

---

# Create Tables

```bash id="4ttjlwm"
docker exec -it farm_fastapi python -m app.database.init_db
```

Expected output:

```text id="xrzb0h"
Creating database tables...
Tables created successfully
```

---

# 🗄️ Verify PostgreSQL Tables

Enter PostgreSQL container:

```bash id="u8cvv8"
docker exec -it farm_postgres psql -U farmadmin -d farm_inventory
```

Inside PostgreSQL:

```sql id="j6mjlwm"
\dt
```

Expected tables:

* inventory
* prediction_history
* inventory_usage

---

# 🌱 Rich Sample Data Generation

Analytics-ready demo data is generated inside the FastAPI container.

---

# Generate Sample Data

```bash id="n1hm8m"
docker exec -it farm_fastapi python -m scripts.generate_sample_data
```

Expected output:

```text id="u7r6f9"
Inventory data generated
Prediction history generated
Inventory usage generated
Rich sample data generated successfully
```

---

# 📊 Dashboard Analytics

The Dockerized dashboard includes:

* Inventory overview
* Prediction analytics
* Low stock alerts
* Crop-wise inventory charts
* Supplier distribution analytics
* Prediction history tracking
* Inventory valuation metrics

---

# 🌐 NGINX Reverse Proxy Integration

NGINX is used as a centralized ingress gateway.

---

# 🔀 Reverse Proxy Routing

| Route | Destination         |
| ----- | ------------------- |
| /     | Streamlit Dashboard |
| /api  | FastAPI APIs        |
| /docs | FastAPI Swagger UI  |

---

# 📁 NGINX Configuration

NGINX configuration is mounted into the container using:

```yaml id="grk4v1"
volumes:
  - ./nginx/default.conf:/etc/nginx/conf.d/default.conf
```

---

# 🌍 Local Domain Routing

The platform is accessible using:

```text id="o94tt4"
farm-ml.local
```

instead of raw IP addresses.

---

# 🖥️ Windows Host Machine Configuration

The Windows host machine must be on the same local network as the VM.

---

# ✏️ Configure Windows Hosts File

Open as Administrator:

```text id="l7k2rf"
C:\Windows\System32\drivers\etc\hosts
```

Add:

```text id="yfq3te"
<VM_IP_ADDRESS>    farm-ml.local
```

Example:

```text id="rqnjgl"
192.168.29.9    farm-ml.local
```

---

# 🔄 Flush Windows DNS Cache

Run CMD as Administrator:

```cmd id="ogtx8f"
ipconfig /flushdns
```

---

# 📡 Access URLs

## Streamlit Dashboard

```text id="r6vjlwm"
http://farm-ml.local
```

---

## FastAPI Swagger UI

```text id="td0o7h"
http://farm-ml.local/docs
```

---

## FastAPI API Root

```text id="w4iwc2"
http://farm-ml.local/api
```

---

# 🔁 Disaster Recovery Validation

The platform was validated using full infrastructure reset testing.

---

# Remove Entire Stack and Volumes

```bash id="uy8tzx"
docker compose down -v
```

This removes:

* containers
* networks
* volumes
* PostgreSQL persistent data

---

# Full Recovery Validation

The entire platform was successfully recreated using:

* container rebuilds
* database initialization
* sample data regeneration
* Docker orchestration

This validated:

* persistence architecture
* recovery workflows
* operational resilience

---

# 🧠 Infrastructure Concepts Implemented

Phase 2 demonstrates:

* Containerized microservice architecture
* Docker Compose orchestration
* Internal Docker networking
* Reverse proxy routing
* Persistent PostgreSQL storage
* Production-style ingress gateway
* Dynamic service communication
* ML model retraining inside containers
* Disaster recovery validation
* Local DNS-style routing
* Windows-to-VM infrastructure integration

---

# 📌 Phase 2 Achievements

✅ Full Dockerized Infrastructure
✅ Multi-Container Architecture
✅ Persistent PostgreSQL Storage
✅ NGINX Reverse Proxy
✅ Internal Service Networking
✅ Local Domain Routing
✅ Dockerized FastAPI
✅ Dockerized Streamlit
✅ Disaster Recovery Validation
✅ Production-Style Gateway Architecture
✅ Operational Infrastructure Testing

---

# 🔮 Next Phase

Phase 3 introduces enterprise MLOps capabilities:

* MLflow integration
* MinIO artifact storage
* Experiment tracking
* Model registry
* Artifact versioning
* Dynamic model loading
* Centralized model management
