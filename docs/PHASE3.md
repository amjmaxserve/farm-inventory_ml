# Phase 3 - Machine Learning & MLOps Foundation

## Objective

The objective of Phase 3 was to transform the Farm Inventory Management platform into an end-to-end Machine Learning and MLOps solution.

The system now supports:

* Data generation
* Dataset creation
* Model training
* Model versioning
* Artifact storage
* ML experiment tracking
* Automated platform bootstrap

---

# Architecture

```text
PostgreSQL
    │
    ▼
Sample Data Generator
    │
    ▼
Training Dataset Export
    │
    ▼
Model Training Pipeline
    │
    ├── Random Forest
    └── XGBoost
    │
    ▼
Best Model Selection
    │
    ├── MLflow Tracking
    ├── MinIO Artifact Storage
    └── Model Metadata
    │
    ▼
FastAPI Prediction API
    │
    ▼
Streamlit Dashboard
```

---

# Components

## PostgreSQL

Stores:

* Inventory records
* Inventory usage history
* Prediction history
* MLflow backend metadata

Database:

```text
farm_inventory
```

---

## MinIO

Object storage used for:

```text
farm-inventory-model-registry/
├── current/
├── versions/
├── datasets/
├── metadata/
└── mlflow/
```

Stores:

* Current production model
* Historical model versions
* Training datasets
* Model metadata
* MLflow artifacts

---

## MLflow

Used for:

* Experiment tracking
* Parameter logging
* Metric logging
* Artifact management

Tracked metrics:

* MAE
* RMSE
* R²

Experiment:

```text
Farm Inventory Prediction
```

---

# Bootstrap Workflow

When the platform starts from scratch:

```text
docker-compose down -v
docker-compose up
```

The following sequence is executed:

1. PostgreSQL starts
2. MinIO starts
3. MLflow starts
4. Bootstrap service starts
5. Database tables are created
6. Sample data is generated
7. Dataset is exported
8. Models are trained
9. Best model is selected
10. Artifacts are uploaded to MinIO
11. Bootstrap exits successfully
12. FastAPI starts
13. Streamlit starts
14. Nginx starts

---

# Machine Learning Pipeline

## Dataset

Source:

```text
datasets/retraining_dataset.csv
```

Contains:

* Crop Type
* Season
* Soil Type
* Rainfall
* Temperature
* Humidity
* Farm Size
* Previous Usage

Target:

```text
required_inventory
```

---

## Models

### Random Forest

Used as baseline model.

### XGBoost

Used as advanced ensemble model.

---

## Model Selection

The model with the highest:

```text
R² Score
```

is selected as the production model.

---

# Model Artifacts

Production model:

```text
current/current_model.pkl
```

Versioned models:

```text
versions/model_<timestamp>.pkl
```

Metadata:

```text
metadata/model_metadata.txt
```

---

# Prediction API

Endpoint:

```text
POST /predict
```

Workflow:

1. Download model from MinIO
2. Load model into memory
3. Perform prediction
4. Save prediction history
5. Return prediction response

---

# Technologies Used

* Python 3.12
* FastAPI
* Streamlit
* PostgreSQL
* MinIO
* MLflow
* Scikit-Learn
* XGBoost
* Docker
* Docker Compose
* Nginx

---

# Phase 3 Outcome

Successfully implemented:

* Machine Learning pipeline
* Automated retraining workflow
* Model versioning
* Artifact management
* Experiment tracking
* End-to-end MLOps foundation

The platform is now ready for Phase 4 enhancements such as:

* MLflow Model Registry
* Scheduled retraining
* Drift detection
* CI/CD integration
* Monitoring and observability
