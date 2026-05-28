# 🌾 Farm Inventory MLOps Platform

An enterprise-style Agriculture Inventory Management and MLOps Platform built using:

* FastAPI
* Streamlit
* PostgreSQL
* Docker
* Scikit-learn
* XGBoost
* SQLAlchemy
* Plotly

This project combines:

* Inventory Management
* Agriculture Analytics
* Machine Learning Predictions
* MLOps Retraining Pipelines
* Operational Dashboards
* PostgreSQL Data Engineering

---

# 🚀 Features

## 📦 Inventory Management

* Add inventory items
* Inventory categorization
* Crop-wise inventory tracking
* Supplier management
* Storage location tracking
* Seasonal inventory management
* Low stock monitoring
* Inventory valuation

---

## 🤖 Machine Learning Prediction

Predict inventory requirements using:

* Crop Type
* Season
* Soil Type
* Rainfall
* Temperature
* Humidity
* Farm Size
* Previous Usage

Supports:

* RandomForest Regressor
* XGBoost Regressor

---

## 📈 Analytics Dashboard

Interactive analytics dashboard using Streamlit and Plotly.

Includes:

* Inventory Distribution
* Crop-wise Analytics
* Supplier Analytics
* Rainfall Impact Analysis
* Temperature Impact Analysis
* Prediction Trends
* Humidity Distribution
* Low Stock Alerts

---

## 🔄 MLOps Retraining Pipeline

Production-style ML retraining workflow:

* Dataset export
* Feature engineering
* OneHotEncoding
* Model comparison
* Automatic best-model selection
* Model persistence
* Prediction logging

---

# 🏗️ System Architecture

```text
                        ┌────────────────────┐
                        │    Streamlit UI    │
                        │ Analytics Dashboard│
                        └─────────┬──────────┘
                                  │
                                  ▼
                        ┌────────────────────┐
                        │      FastAPI       │
                        │ Prediction API     │
                        │ Inventory API      │
                        └─────────┬──────────┘
                                  │
             ┌────────────────────┴────────────────────┐
             ▼                                         ▼
    ┌─────────────────┐                     ┌──────────────────┐
    │ PostgreSQL DB   │                     │ ML Models        │
    │ Inventory Data  │                     │ RandomForest     │
    │ Usage Tracking  │                     │ XGBoost          │
    │ Prediction Logs │                     └──────────────────┘
    └─────────────────┘
```

---

# 🧠 ML Pipeline

## Feature Engineering

### Categorical Features

* crop_type
* season
* soil_type

### Numerical Features

* rainfall
* temperature
* humidity
* farm_size
* previous_usage

---

## Model Training Pipeline

Uses:

* ColumnTransformer
* Pipeline
* OneHotEncoder
* SimpleImputer

---

## Model Comparison

The system automatically compares:

* RandomForestRegressor
* XGBoostRegressor

Best-performing model is selected automatically.

---

# 🗄️ Database Schema

## inventory

Stores:

* inventory items
* stock levels
* suppliers
* seasonal data
* warehouse locations

---

## prediction_history

Stores:

* prediction requests
* ML outputs
* model versions
* confidence scores

---

## inventory_usage

Stores:

* inventory consumption
* crop usage patterns
* seasonal usage
* operational tracking

---

# 🐳 Dockerized PostgreSQL

Database runs inside Docker container.

## Start PostgreSQL

```bash
docker compose up -d
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone git@github.com:amjmaxserve/farm-inventory_ml.git
```

---

## 2. Enter Project

```bash
cd farm-inventory_ml
```

---

## 3. Create Virtual Environment

```bash
python3 -m venv venv
```

---

## 4. Activate Environment

### Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\\Scripts\\activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄️ Database Setup

## Start PostgreSQL

```bash
docker compose up -d
```

---

## Initialize Tables

```bash
python -m app.database.init_db
```

---

# 📊 Generate Rich Sample Data

```bash
python -m scripts.generate_sample_data
```

This generates:

* Inventory records
* Prediction history
* Usage analytics data

---

# 🤖 Retrain ML Models

## Export Dataset

```bash
python -m scripts.export_training_dataset
```

---

## Retrain Models

```bash
python -m app.ml.retrain_model
```

---

# 🚀 Run Backend API

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

# 🎨 Run Streamlit Dashboard

```bash
streamlit run frontend/streamlit_app/app.py
```

Dashboard:

```text
http://localhost:8501
```

---

# 📂 Project Structure

```text
farm_inventory_ml/
│
├── app/
│   ├── api/
│   ├── database/
│   ├── ml/
│   └── schemas/
│
├── frontend/
│   └── streamlit_app/
│
├── scripts/
│
├── datasets/
│
├── trained_models/
│
├── docker-compose.yml
├── main.py
├── requirements.txt
└── README.md
```

---

# 📌 Current Capabilities

✅ Inventory Management
✅ Agriculture Analytics
✅ Machine Learning Predictions
✅ PostgreSQL Integration
✅ Dockerized Database
✅ Feature Engineering
✅ Automated Retraining
✅ Model Comparison
✅ Streamlit Dashboard
✅ Operational Analytics
✅ Prediction Logging
✅ Low Stock Alerts

---

# 🔮 Future Enhancements

## Security

* JWT Authentication
* RBAC
* User Management

---

## DevOps

* Dockerized APIs
* Nginx Reverse Proxy
* GitHub Actions CI/CD
* Kubernetes Deployment

---

## Advanced MLOps

* MLflow Integration
* Drift Detection
* Scheduled Retraining
* Model Registry
* Grafana Monitoring
* Prometheus Metrics

---

# 📈 Tech Stack

| Category         | Technology            |
| ---------------- | --------------------- |
| Backend          | FastAPI               |
| Frontend         | Streamlit             |
| Database         | PostgreSQL            |
| ORM              | SQLAlchemy            |
| ML               | Scikit-learn, XGBoost |
| Visualization    | Plotly                |
| Containerization | Docker                |
| Language         | Python                |

---

# 👨‍💻 Author

Arjun M J

DevOps Engineer | Cloud Architect | MLOps Enthusiast

GitHub:
https://github.com/amjmaxserve

---

# ⭐ Project Status

Current Stage:

```text
Intermediate Enterprise Agriculture MLOps Platform
```

This project is actively evolving toward a full production-grade MLOps ecosystem.
