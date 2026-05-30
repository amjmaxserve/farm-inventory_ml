# 🌾 Farm Inventory MLOps Platform

An enterprise-style Agriculture Inventory Management and MLOps platform built using:

* FastAPI
* Streamlit
* PostgreSQL
* Docker
* NGINX
* Scikit-learn
* XGBoost
* SQLAlchemy
* Plotly

---

# 🚀 Project Overview

This platform combines:

* Inventory Management
* Agriculture Analytics
* Machine Learning Predictions
* MLOps Retraining Pipelines
* Operational Dashboards
* PostgreSQL Data Engineering
* Containerized Infrastructure
* Reverse Proxy Architecture

---

# 🏗️ Current Architecture

```text
                    farm-ml.local
                           │
                    ┌────────────┐
                    │   NGINX    │
                    └─────┬──────┘
                          │
        ┌─────────────────┼─────────────────┐
        ▼                                   ▼
 ┌────────────┐                     ┌────────────┐
 │ Streamlit  │                     │  FastAPI   │
 └────────────┘                     └─────┬──────┘
                                          ▼
                                 ┌────────────────┐
                                 │ PostgreSQL DB  │
                                 └────────────────┘
```

---

# 📚 Documentation

## 🔹 Phase 1 — Core Platform Development

Includes:

* FastAPI APIs
* PostgreSQL integration
* ML model training
* Retraining pipeline
* Streamlit analytics dashboard
* Sample data generation

👉 [Read PHASE1 Documentation](docs/PHASE1.md)

---

## 🔹 Phase 2 — Docker & Infrastructure

Includes:

* Full Dockerized stack
* Docker Compose orchestration
* PostgreSQL persistence
* NGINX reverse proxy
* Local domain routing
* Disaster recovery testing
* Windows host integration

👉 [Read PHASE2 Documentation](docs/PHASE2.md)

---

# 📈 Current Capabilities

✅ Inventory Management
✅ ML Predictions
✅ Streamlit Analytics
✅ PostgreSQL Persistence
✅ Dockerized Infrastructure
✅ Reverse Proxy Architecture
✅ Automated Retraining
✅ Rich Analytics Dashboard
✅ Local Domain Routing

---



## 🔹 Phase 3 — Machine Learning & MLOps Foundation

Implemented:

### Machine Learning

* Automated dataset generation
* Training dataset export pipeline
* Random Forest model training
* XGBoost model training
* Automated best model selection
* Production model promotion

### MLflow Integration

* MLflow Tracking Server
* PostgreSQL backend store
* Experiment management
* Parameter tracking
* Metric tracking
* Artifact tracking

Tracked Metrics:

* MAE
* RMSE
* R² Score

### MinIO Integration

* Model artifact storage
* Dataset storage
* Metadata storage
* Versioned model storage
* Current production model storage

Bucket Structure:

```text
farm-inventory-model-registry/
├── current/
├── versions/
├── datasets/
├── metadata/
└── mlflow/
```

### Bootstrap Automation

Complete platform initialization workflow:

```text
PostgreSQL
    ↓
MinIO
    ↓
MLflow
    ↓
Bootstrap
    ↓
Create Tables
    ↓
Generate Sample Data
    ↓
Export Dataset
    ↓
Train Models
    ↓
Select Best Model
    ↓
Upload Artifacts
    ↓
FastAPI
    ↓
Streamlit
    ↓
NGINX
```

### MLOps Features

✅ Experiment Tracking

✅ Model Versioning

✅ Artifact Management

✅ Automated Training Pipeline

✅ Automated Platform Bootstrap

✅ Object Storage Integration

👉 Read Full Documentation: docs/PHASE3.md

---

# 🔮 Upcoming Phases

## Phase 4 — DevOps & CI/CD

Planned:

* GitHub Actions
* Automated Testing
* CI/CD Pipelines
* Production Deployment
* Kubernetes

---

# 👨‍💻 Author

Arjun M J

DevOps Engineer | Cloud Architect | MLOps Enthusiast

GitHub:
https://github.com/amjmaxserve

---

# ⭐ Project Status

```text
Enterprise Agriculture MLOps Platform
```

Actively evolving toward a production-grade scalable MLOps ecosystem.
