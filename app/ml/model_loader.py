import os
import boto3
from app.config import *
from app.core.logger import get_logger

logger = get_logger("fastapi")
MODEL_PATH = "trained_models/current_model.pkl"

BUCKET_NAME = MODEL_BUCKET

MINIO_URL = (
    f"http://{MINIO_ENDPOINT}"
)

AWS_ACCESS_KEY_ID = MINIO_ROOT_USER
AWS_SECRET_ACCESS_KEY = MINIO_ROOT_PASSWORD


def download_latest_model():

    os.makedirs(
        "trained_models",
        exist_ok=True
    )

    s3_client = boto3.client(
        "s3",
        endpoint_url=MINIO_URL,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )

    logger.info("Downloading the latest model from MinIO...")

    s3_client.download_file(
        BUCKET_NAME,
        "current/current_model.pkl",
        MODEL_PATH
    )

    logger.info("Latest model downloaded successfully")

    return MODEL_PATH