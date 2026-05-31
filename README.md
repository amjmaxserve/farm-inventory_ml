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

## 🔹 Phase 4 — Testing, Quality Assurance & CI/CD

Implemented:

### Automated Testing

* Pytest-based test suite
* Health API testing
* Inventory API testing
* Prediction API testing
* Dockerized testing environment

### Code Quality

* Flake8 integration
* Pydantic V2 migration
* Deprecated code cleanup
* Automated code validation

### Logging & Observability

* Centralized logging framework
* Component-specific log files
* FastAPI request logging
* Bootstrap process logging
* Retraining process logging

Log Structure:

```text
logs/
├── fastapi.log
├── Bootstrap.log
└── Retraining.log
```

### CI/CD Pipeline

Implemented GitHub Actions workflow with:

* Automated code validation
* Automated testing
* Self-hosted GitHub Runner
* Environment validation
* GitHub Secrets integration

Pipeline Flow:

```text
Git Push
    ↓
GitHub Actions
    ↓
Self Hosted Runner
    ↓
Flake8
    ↓
Pytest
    ↓
Pass / Fail
```

### Security Enhancements

* GitHub Secrets Management
* Environment-based configuration
* Secure credential handling

### Architecture Improvements

* Lazy model loading
* Faster API startup
* Reduced dependency coupling
* Improved testability

### Testing Results

```text
3 Tests Executed
3 Tests Passed
0 Failures
```

### Phase 4 Achievements

✅ Automated Testing

✅ Dockerized Testing

✅ Flake8 Validation

✅ GitHub Actions CI

✅ Self-Hosted Runner

✅ GitHub Secrets

✅ Centralized Logging

✅ Lazy Model Loading

👉 Read Full Documentation: docs/PHASE4.md

---

## 📈 Current Capabilities

✅ Inventory Management

✅ Machine Learning Predictions

✅ Automated Retraining

✅ MLflow Experiment Tracking

✅ Model Registry using MinIO

✅ Streamlit Analytics Dashboard

✅ PostgreSQL Persistence

✅ Dockerized Infrastructure

✅ NGINX Reverse Proxy

✅ Local Domain Routing

✅ Centralized Logging

✅ Automated Testing

✅ GitHub Actions CI/CD

✅ Self-Hosted Runner

✅ Model Versioning

✅ Production Model Promotion

---

# 🔮 Upcoming Phases

## Phase 5 — Security & Production Readiness

Planned:

* JWT Authentication
* Role Based Access Control (RBAC)
* API Security Hardening
* Prometheus Monitoring
* Grafana Dashboards
* Backup & Recovery Automation

---

## Phase 6 — Kubernetes & Cloud Deployment

Planned:

* Kubernetes Deployment
* Helm Charts
* Horizontal Scaling
* Ingress Controllers
* GitOps Deployment
* Cloud Infrastructure Integration

---

## Phase 7 — Enterprise MLOps

Planned:

* Automated Retraining Schedules
* Drift Detection
* Model Monitoring
* Feature Store
* A/B Model Testing
* Advanced MLOps Automation
* Multi-Environment Deployment

```

---
```

