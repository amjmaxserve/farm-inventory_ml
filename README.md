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


## 🔹 Phase 5 — Security, Authentication & Governance

Implemented:

### Authentication

* OAuth2 Password Flow
* JWT Access Tokens
* Swagger Authorization Integration
* Secure Password Hashing using bcrypt

### Authorization (RBAC)

Supported Roles:

* ADMIN
* INVENTORY_MANAGER
* DATA_SCIENTIST
* VIEWER

Access Controls:

* User Management APIs
* Inventory APIs
* Prediction APIs
* Prediction History APIs

### User Management

Implemented APIs:

* Create User
* List Users
* Get User
* Update User
* Enable User
* Disable User
* Delete User

### Audit Logging

Implemented:

* PostgreSQL Audit Log Table
* User Creation Auditing
* User Update Auditing
* User Enable Auditing
* User Disable Auditing
* User Delete Auditing

Audit Table Structure:

```text
audit_logs
├── id
├── username
├── action
├── resource
├── details
└── created_at
```

### Security Features

✅ OAuth2 Authentication

✅ JWT Authorization

✅ Role Based Access Control

✅ User Lifecycle Management

✅ Audit Logging

✅ Swagger OAuth2 Integration

### Phase 5 Achievements

```text
Authentication Layer
        ↓
Authorization Layer
        ↓
Role Based Access Control
        ↓
User Governance
        ↓
Audit Logging
```

👉 Read Full Documentation: docs/PHASE5.md

---

## 📈 Current Capabilities

✅ Inventory Management

✅ Machine Learning Predictions

✅ Automated Retraining

✅ MLflow Experiment Tracking

✅ MinIO Model Registry

✅ Streamlit Analytics Dashboard

✅ PostgreSQL Persistence

✅ Dockerized Infrastructure

✅ NGINX Reverse Proxy

✅ Centralized Logging

✅ Automated Testing

✅ GitHub Actions CI/CD

✅ OAuth2 Authentication

✅ JWT Authorization

✅ Role Based Access Control

✅ User Administration

✅ Audit Logging

✅ Model Versioning

✅ Production Model Promotion

---


## 🔹 Phase 6 — Advanced MLOps & Model Governance

Implemented:

### Model Registry

* Centralized Model Registry
* Model Version Tracking
* Production Model Tracking
* Staging Model Tracking

### Model Registry APIs

Implemented APIs:

* Register Model
* List Models
* Get Current Production Model
* Promote Model Version

### Model Promotion Workflow

Supported Lifecycle:

```text
Register Model
      ↓
STAGING
      ↓
Promote
      ↓
PRODUCTION
```

### Automatic Production Selection

Implemented:

* First registered model automatically becomes PRODUCTION
* Subsequent models registered as STAGING
* Controlled model promotion workflow

### Model Governance

Implemented:

* Model Version Management
* Production Model Tracking
* Model Lifecycle Governance
* Promotion Audit Trail

### Model Promotion Audit Logging

Audit entries created for:

* Model Promotion
* Production Model Changes

Audit Example:

```text
admin
PROMOTE_MODEL
MODEL_REGISTRY
Promoted model version v2 to PRODUCTION
```

### Phase 6 Achievements

✅ Model Registry

✅ Model Version APIs

✅ Production Model Tracking

✅ Model Promotion APIs

✅ Model Governance

✅ Promotion Audit Logging

✅ RBAC Protected Model Operations

👉 Read Full Documentation: docs/PHASE6.md

---
# 🔮 Upcoming Phases


## Phase 7 — Kubernetes & Cloud Native Deployment

Planned:

* Kubernetes Deployment
* Helm Charts
* Horizontal Scaling
* Ingress Controllers
* GitOps Deployment
* Cloud Infrastructure Integration

---

## Phase 8 — Enterprise MLOps Platform

Planned:

* Feature Store
* Model Serving Gateway
* A/B Model Testing
* Canary Model Releases
* Multi-Environment Promotion
* Enterprise Governance
* Advanced Observability

```


