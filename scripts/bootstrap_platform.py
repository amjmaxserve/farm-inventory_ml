import time
import subprocess
import requests

from sqlalchemy import text

from app.database.db import SessionLocal

from app.config import (
    MINIO_HEALTH_URL,
    MLFLOW_HEALTH_URL
)

from app.core.logger import get_logger

logger = get_logger("Bootstrap")

def wait_for_postgres():

    logger.info("Waiting for PostgreSQL...")

    while True:

        try:

            db = SessionLocal()

            db.execute(text("SELECT 1"))

            db.close()

            logger.info("PostgreSQL Ready")

            return

        except Exception as e:

            print(e)

            time.sleep(5)


def wait_for_minio():

    print("Waiting for MinIO...")

    while True:

        try:

            response = requests.get(
                MINIO_HEALTH_URL
            )

            if response.status_code == 200:

                print("MinIO Ready")

                return

        except Exception:

            pass

        time.sleep(5)

def wait_for_mlflow():

    print("Waiting for MLflow...")

    while True:
        try:
            
            response = requests.get(
                MLFLOW_HEALTH_URL
            )

            if response.status_code == 200:

                print("MLflow Ready")

                return
        except Exception:
            
            pass
        
        time.sleep(5)

def create_tables():

    print("Creating tables...")

    subprocess.run(
        [
            "python",
            "-m",
            "app.database.init_db"
        ],
        check=True
    )


def generate_sample_data():

    print("Generating sample data...")

    subprocess.run(
        [
            "python",
            "-m",
            "scripts.generate_sample_data"
        ],
        check=True
    )


def export_dataset():

    print("Exporting training dataset...")

    subprocess.run(
        [
            "python",
            "-m",
            "scripts.export_training_dataset"
        ],
        check=True
    )


def train_model():

    print("Training model and uploading to MinIO...")

    subprocess.run(
        [
            "python",
            "-m",
            "app.ml.retrain_model"
        ],
        check=True
    )


if __name__ == "__main__":

    print("\nBOOTSTRAP STARTED\n")

    wait_for_postgres()

    wait_for_minio()
    
    wait_for_mlflow()

    create_tables()

    generate_sample_data()

    export_dataset()

    train_model()

    print("\nBOOTSTRAP COMPLETED\n")