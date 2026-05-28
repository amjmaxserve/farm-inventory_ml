# 🌾 Phase 1 — Core Platform Development

This phase focuses on building the core Farm Inventory Management and Machine Learning platform.

---

# 🎯 Objectives

Phase 1 implemented:

* Inventory Management APIs
* PostgreSQL integration
* Machine Learning prediction engine
* Model retraining pipeline
* Streamlit analytics dashboard
* Operational analytics
* Rich sample data generation

---

# 🏗️ Core Architecture

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
             ┌────────────────┴────────────────┐
             ▼                                 ▼
    ┌─────────────────┐              ┌──────────────────┐
    │ PostgreSQL DB   │              │ ML Models        │
    │ Inventory Data  │              │ RandomForest     │
    │ Usage Tracking  │              │ XGBoost          │
    │ Prediction Logs │              └──────────────────┘
    └─────────────────┘
```

---

# 🚀 Features

## 📦 Inventory Management

Implemented capabilities:

* Add inventory items
* Inventory categorization
* Crop-wise inventory tracking
* Supplier management
* Storage location tracking
* Seasonal inventory management
* Low stock monitoring
* Inventory valuation

---

# 🤖 Machine Learning Prediction

The platform predicts future inventory requirements using:

* Crop Type
* Season
* Soil Type
* Rainfall
* Temperature
* Humidity
* Farm Size
* Previous Usage

---

# 🧠 ML Models

Implemented models:

* RandomForestRegressor
* XGBoostRegressor

The platform automatically compares models and selects the best-performing one.

---

# 📈 Analytics Dashboard

Interactive Streamlit dashboard includes:

* Inventory Distribution
* Crop-wise Analytics
* Supplier Analytics
* Rainfall Impact Analysis
* Temperature Impact Analysis
* Prediction Trends
* Humidity Distribution
* Low Stock Alerts
* Inventory Valuation

Visualization libraries:

* Plotly
* Pandas
* Streamlit Charts

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

# ⚙️ Training Pipeline Components

The retraining pipeline uses:

* ColumnTransformer
* Pipeline
* OneHotEncoder
* SimpleImputer
* RandomForestRegressor
* XGBoostRegressor

---

# 🔄 Retraining Workflow

Implemented retraining workflow:

1. Export training dataset
2. Feature engineering
3. Train multiple models
4. Compare performance
5. Select best model
6. Save trained model
7. Enable prediction serving

---

# 🗄️ Database Schema

## inventory

Stores:

* Inventory items
* Stock levels
* Suppliers
* Warehouse locations
* Seasonal inventory data

---

## prediction_history

Stores:

* Prediction requests
* ML prediction outputs
* Prediction timestamps

---

## inventory_usage

Stores:

* Inventory consumption history
* Crop usage tracking
* Seasonal operational analytics

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone git@github.com:amjmaxserve/farm-inventory_ml.git
```

---

## 2️⃣ Enter Project

```bash
cd farm-inventory_ml
```

---

## 3️⃣ Create Virtual Environment

```bash
python3 -m venv venv
```

---

## 4️⃣ Activate Environment

### Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\\Scripts\\activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄️ PostgreSQL Setup

## Start PostgreSQL Container

```bash
docker compose up -d
```

---

# 🛠️ Initialize Database

Create all required tables:

```bash
python -m app.database.init_db
```

Expected output:

```text
Creating database tables...
Tables created successfully
```

---

# 📊 Generate Rich Sample Data

Generate analytics-ready data:

```bash
python -m scripts.generate_sample_data
```

This generates:

* Inventory records
* Prediction history
* Inventory usage data
* Crop analytics data
* Supplier distribution data

Expected output:

```text
Inventory data generated
Prediction history generated
Inventory usage generated
Rich sample data generated successfully
```

---

# 🤖 Export ML Dataset

```bash
python -m scripts.export_training_dataset
```

This creates:

```text
datasets/training_data.csv
```

---

# 🧠 Retrain ML Models

```bash
python -m app.ml.retrain_model
```

The retraining pipeline:

* Loads dataset
* Performs preprocessing
* Trains multiple models
* Compares performance
* Saves best model

Generated model files:

```text
trained_models/
```

Example:

```text
random_forest_model.pkl
current_model.pkl
```

---

# 🚀 Run FastAPI Backend

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

# 📘 Swagger UI

```text
http://localhost:8000/docs
```

---

# 🎨 Run Streamlit Dashboard

```bash
streamlit run frontend/streamlit_app/app.py
```

---

# 📊 Streamlit Dashboard URL

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

# 📌 Phase 1 Achievements

✅ FastAPI Backend APIs
✅ PostgreSQL Integration
✅ Inventory Management
✅ Machine Learning Prediction Engine
✅ Retraining Pipeline
✅ Automated Model Selection
✅ Streamlit Analytics Dashboard
✅ Operational Analytics
✅ Sample Data Generation
✅ Prediction Logging
✅ Low Stock Alert System

---

# 🔮 Next Phase

Phase 2 introduces:

* Full Dockerized deployment
* NGINX reverse proxy
* Local domain routing
* Persistent infrastructure
* Disaster recovery testing
* Production-style networking
