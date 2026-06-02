# Phase 6 — Advanced MLOps & Model Governance

## Overview

Phase 6 introduced enterprise-grade MLOps governance capabilities to the Farm Inventory Management Platform.

The objective of this phase was to establish a complete model lifecycle management system, allowing machine learning models to be registered, versioned, promoted, governed, and audited without modifying application code.

---

# Objectives

* Implement Model Registry
* Support Model Version Management
* Support Model Promotion Workflow
* Introduce Model Governance
* Enable Audit Logging for Model Operations
* Prepare platform for production-grade MLOps

---

# Architecture

```text
Training Pipeline
        │
        ▼
   MLflow Run
        │
        ▼
 Model Registry
        │
 ┌──────┴──────┐
 ▼             ▼
STAGING    PRODUCTION
        │
        ▼
 Prediction API
```

---

# 6.1 Model Registry Database

## ModelRegistry Table

Created a centralized model registry table.

### Columns

| Column        | Description             |
| ------------- | ----------------------- |
| id            | Primary Key             |
| model_name    | Name of model           |
| version       | Version identifier      |
| mlflow_run_id | MLflow run reference    |
| artifact_path | Model artifact location |
| accuracy      | Model accuracy          |
| status        | STAGING / PRODUCTION    |
| created_at    | Creation timestamp      |

---

# 6.2 Model Registry APIs

## List Models

```http
GET /api/models
```

Returns all registered models.

### Example Response

```json
[
  {
    "version": "v1",
    "status": "PRODUCTION"
  },
  {
    "version": "v2",
    "status": "STAGING"
  }
]
```

---

## Current Production Model

```http
GET /api/models/current
```

Returns the active production model.

### Example Response

```json
{
  "version": "v1",
  "status": "PRODUCTION"
}
```

---

# 6.3 Model Registration

## Register Model

```http
POST /api/models
```

### Example Request

```json
{
  "model_name": "inventory_predictor",
  "version": "v2",
  "mlflow_run_id": "run_002",
  "artifact_path": "models/inventory/v2/model.pkl",
  "accuracy": 0.97
}
```

### Features

* Duplicate version validation
* Automatic model registration
* RBAC protected endpoint
* Data Scientist access control

---

## Automatic Production Selection

Logic implemented:

### First Model

```text
v1 → PRODUCTION
```

### Additional Models

```text
v1 → PRODUCTION
v2 → STAGING
v3 → STAGING
```

This prevents accidental replacement of production models.

---

# 6.4 Model Promotion

## Promote Model

```http
POST /api/models/promote/{version}
```

### Example

```http
POST /api/models/promote/v2
```

### Before Promotion

```text
v1 → PRODUCTION
v2 → STAGING
```

### After Promotion

```text
v1 → STAGING
v2 → PRODUCTION
```

### Benefits

* Zero code changes
* Zero deployment changes
* Controlled model lifecycle
* Rollback support

---

# 6.5 Audit Logging

Every promotion action is recorded.

## Example

```text
Username : admin
Action   : PROMOTE_MODEL
Resource : MODEL_REGISTRY
Details  : Promoted model version v2 to PRODUCTION
```

---

## Audit Log Query

```sql
SELECT
username,
action,
resource,
details
FROM audit_logs
ORDER BY id DESC;
```

---

# Security Controls

## RBAC

Protected endpoints require:

```text
ADMIN
DATA_SCIENTIST
```

roles.

---

## Authentication

JWT Bearer Authentication

```http
Authorization: Bearer <token>
```

---

# Testing Performed

## Model Registration

Passed

```text
POST /api/models
```

---

## Model Promotion

Passed

```text
POST /api/models/promote/v1
POST /api/models/promote/v2
```

---

## Model Listing

Passed

```text
GET /api/models
GET /api/models/current
```

---

## Audit Verification

Passed

```sql
SELECT * FROM audit_logs;
```

---

# Deliverables Completed

✅ Model Registry Database

✅ Model Version Tracking

✅ Model Registration API

✅ Automatic Production Selection

✅ Model Promotion API

✅ Audit Logging

✅ RBAC Integration

✅ Governance Workflow

---

# Current Platform Status

```text
Farm Inventory Platform

├── FastAPI
├── PostgreSQL
├── MLflow
├── MinIO
├── Streamlit
├── Docker
├── Nginx
├── GitHub Actions CI
├── JWT Authentication
├── RBAC
├── Audit Logging
├── Inventory Management
├── Prediction Engine
├── Model Registry
└── Model Promotion Workflow
```

---

# Phase 6 Outcome

Phase 6 transformed the project from a simple ML application into an enterprise-style MLOps platform with governed model lifecycle management.

The platform now supports model registration, versioning, promotion, auditing, and controlled deployment workflows.

Status: COMPLETED
