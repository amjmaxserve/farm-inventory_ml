import os

from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = os.getenv(
    "POSTGRES_USER"
)

POSTGRES_PASSWORD = os.getenv(
    "POSTGRES_PASSWORD"
)

POSTGRES_DB = os.getenv(
    "POSTGRES_DB"
)

POSTGRES_HOST = os.getenv(
    "POSTGRES_HOST"
)

POSTGRES_PORT = os.getenv(
    "POSTGRES_PORT"
)

MINIO_ROOT_USER = os.getenv(
    "MINIO_ROOT_USER"
)

MINIO_ROOT_PASSWORD = os.getenv(
    "MINIO_ROOT_PASSWORD"
)

MINIO_ENDPOINT = os.getenv(
    "MINIO_ENDPOINT"
)

MLFLOW_TRACKING_URI = os.getenv(
    "MLFLOW_TRACKING_URI"
)

MODEL_BUCKET = os.getenv(
    "MODEL_BUCKET"
)

MINIO_HEALTH_URL = os.getenv(
    "MINIO_HEALTH_URL"
)

MLFLOW_HEALTH_URL = os.getenv(
    "MLFLOW_HEALTH_URL"
)