import os
import boto3

MODEL_PATH = "trained_models/current_model.pkl"

BUCKET_NAME = "farm-inventory-model-registry"

MINIO_ENDPOINT = "http://minio:9000"

AWS_ACCESS_KEY_ID = "minioadmin"
AWS_SECRET_ACCESS_KEY = "minioadmin"


def download_latest_model():

    os.makedirs(
        "trained_models",
        exist_ok=True
    )

    s3_client = boto3.client(
        "s3",
        endpoint_url=MINIO_ENDPOINT,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )

    print(
        "\nDownloading latest model from MinIO..."
    )

    s3_client.download_file(
        BUCKET_NAME,
        "current/current_model.pkl",
        MODEL_PATH
    )

    print(
        "Latest model downloaded successfully"
    )

    return MODEL_PATH