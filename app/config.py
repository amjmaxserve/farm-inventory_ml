import os

from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.getenv(
    "POSTGRES_USER",
    "farmadmin"
)

POSTGRES_PASSWORD = os.getenv(
    "POSTGRES_PASSWORD",
    "StrongPassword123"
)

POSTGRES_DB = os.getenv(
    "POSTGRES_DB",
    "farm_inventory"
)

POSTGRES_HOST = os.getenv(
    "POSTGRES_HOST",
    "postgres"
)

POSTGRES_PORT = os.getenv(
    "POSTGRES_PORT",
    "5432"
)

MINIO_ROOT_USER = os.getenv(
    "MINIO_ROOT_USER",
    "minioadmin"
)

MINIO_ROOT_PASSWORD = os.getenv(
    "MINIO_ROOT_PASSWORD",
    "minioadmin"
)

MINIO_ENDPOINT = os.getenv(
    "MINIO_ENDPOINT",
    "minio:9000"
)

MLFLOW_TRACKING_URI = os.getenv(
    "MLFLOW_TRACKING_URI",
    "http://mlflow:5000"
)

MODEL_BUCKET = os.getenv(
    "MODEL_BUCKET",
    "farm-inventory-model-registry"
)

MINIO_HEALTH_URL = os.getenv(
    "MINIO_HEALTH_URL",
    "http://minio:9000/minio/health/live"
)

MLFLOW_HEALTH_URL = os.getenv(
    "MLFLOW_HEALTH_URL",
    "http://mlflow:5000"
)

JWT_SECRET_KEY = os.getenv(
    "JWT_SECRET_KEY",
    "change-me-in-production"
)

JWT_ALGORITHM = "HS256"

JWT_EXPIRE_MINUTES = 60