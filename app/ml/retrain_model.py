# ======================================
# SECTION 1
# IMPORTS
# ======================================

import os
from datetime import datetime

import importlib
import sys

# Check required third-party packages before importing them so we can
# provide a clear error message if the environment is missing deps.
required_modules = [
    "boto3",
    "pandas",
    "mlflow",
    "xgboost",
    "sklearn",
]
missing = []
for m in required_modules:
    try:
        importlib.import_module(m)
    except Exception:
        missing.append(m)

if missing:
    print("Missing required Python packages:", ", ".join(missing))
    print("Install them with: pip install -r requirements.txt")
    sys.exit(1)

import boto3
try:
    import joblib
    _HAS_JOBLIB = True
except Exception:
    import pickle
    _HAS_JOBLIB = False

def save_model(obj, path):
    """Save model to `path` using joblib if available, otherwise pickle."""
    if _HAS_JOBLIB:
        joblib.dump(obj, path)
    else:
        with open(path, "wb") as f:
            pickle.dump(obj, f)
import pandas as pd
import mlflow


from botocore.exceptions import ClientError

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from xgboost import XGBRegressor
from app.config import *

# ======================================
# SECTION 2
# CONFIGURATION
# ======================================

MLFLOW_URI = MLFLOW_TRACKING_URI

MINIO_ENDPOINT = MINIO_ENDPOINT

BUCKET_NAME = MODEL_BUCKET

DATASET_PATH = "datasets/retraining_dataset.csv"

CURRENT_MODEL_PATH = (
    "trained_models/current_model.pkl"
)

# ======================================
# SECTION 3
# MLFLOW SETUP
# ======================================
os.environ["AWS_ACCESS_KEY_ID"] = MINIO_ROOT_USER
os.environ["AWS_SECRET_ACCESS_KEY"] = MINIO_ROOT_PASSWORD


mlflow.set_tracking_uri(
    MLFLOW_URI
)



mlflow.set_experiment(
    "Farm Inventory Prediction"
)

# ======================================
# SECTION 4
# MINIO CLIENT
# ======================================

s3_client = boto3.client(
    "s3",
    endpoint_url=f"http://{MINIO_ENDPOINT}",
    aws_access_key_id=MINIO_ROOT_USER,
    aws_secret_access_key=MINIO_ROOT_PASSWORD
)

# ======================================
# SECTION 5
# UTILITY FUNCTIONS
# ======================================

def create_bucket_if_not_exists():

    try:

        s3_client.head_bucket(
            Bucket=BUCKET_NAME
        )

        print(
            f"Bucket '{BUCKET_NAME}' already exists."
        )

    except ClientError:

        try:

            s3_client.create_bucket(
                Bucket=BUCKET_NAME
            )

            print(
                f"Bucket '{BUCKET_NAME}' created successfully."
            )

        except Exception as e:

            print(
                f"Bucket creation failed: {e}"
            )

            raise

def create_directories():
    os.makedirs("trained_models", exist_ok=True)
    os.makedirs("datasets", exist_ok=True)
    os.makedirs("tmp_mlflow", exist_ok=True)
    
def load_dataset():
    if not os.path.exists(DATASET_PATH):
        raise FileNotFoundError(f"Dataset not found at path: {DATASET_PATH}")
    
    df = pd.read_csv(DATASET_PATH)
    print("\nDataset loaded successfully: \n")
    print(df.head())
    print(f"\nDataset shape: {df.shape}")
    print(f"Dataset columns: {list(df.columns)}")
    
    return df
    


# ======================================
# SECTION 6
# ENVIRONMENT PREPARATION
# ======================================

create_bucket_if_not_exists()

create_directories()

print("Environment preparation completed.")

# ======================================
# SECTION 7
# LOAD DATASET
# ======================================

df = load_dataset()

# ======================================
# SECTION 8
# FEATURES & TARGET
# ======================================

X = df[
    [
        "crop_type",
        "season",
        "soil_type",
        "rainfall",
        "temperature",
        "humidity",
        "farm_size",
        "previous_usage"
    ]
]

Y = df[
    "predicted_inventory"
]

# ======================================
# SECTION 9
# COLUMN TYPES
# ======================================

categorical_columns = [

    "crop_type",

    "season",

    "soil_type"
]

numerical_columns = [

    "rainfall",

    "temperature",

    "humidity",

    "farm_size",

    "previous_usage"
]

# ======================================
# SECTION 10
# PREPROCESSING PIPELINES
# ======================================

# --------------------------------------
# 10.1 CATEGORICAL PIPELINE
# --------------------------------------

categorical_transformer = Pipeline([

    (
        "imputer",

        SimpleImputer(
            strategy="most_frequent"
        )
    ),

    (
        "encoder",

        OneHotEncoder(
            handle_unknown="ignore"
        )
    )
])


# --------------------------------------
# 10.2 NUMERICAL PIPELINE
# --------------------------------------

numerical_transformer = Pipeline([

    (
        "imputer",

        SimpleImputer(
            strategy="median"
        )
    )
])


# --------------------------------------
# 10.3 COMBINED PREPROCESSOR
# --------------------------------------

preprocessor = ColumnTransformer([

    (
        "cat",

        categorical_transformer,

        categorical_columns
    ),

    (
        "num",

        numerical_transformer,

        numerical_columns
    )
])


print(
    "\nPreprocessing Pipeline Created Successfully"
)


# ======================================
# SECTION 11
# TRAIN TEST SPLIT
# ======================================

X_train, X_test, y_train, y_test = train_test_split(

    X,

    Y,

    test_size=0.2,

    random_state=42
)


print(
    "\nTrain-Test Split Completed"
)

print(
    f"Training Records : {len(X_train)}"
)

print(
    f"Testing Records  : {len(X_test)}"
)


# ======================================
# SECTION 12
# MODEL CANDIDATES
# ======================================

models = {

    "random_forest":

        RandomForestRegressor(

            n_estimators=200,

            random_state=42
        ),

    "xgboost":

        XGBRegressor(

            n_estimators=200,

            learning_rate=0.05,

            max_depth=6,

            random_state=42,

            verbosity=0
        )
}

print(
    "\nCandidate Models Loaded"
)

print(
    f"Total Models: {len(models)}"
)

for model_name in models.keys():

    print(
        f" - {model_name}"
    )
    
# ======================================
# SECTION 13
# BEST MODEL TRACKING
# ======================================

best_model = None

best_model_name = None

best_r2 = -999

best_mae = None

best_rmse = None

best_run_id = None


print(
    "\nBest Model Tracking Initialized"
)

print(
    f"Initial Best R2 Score : {best_r2}"
)

# ======================================
# SECTION 14
# TRAINING LOOP
# ======================================

for model_name, model in models.items():

    print("\n" + "=" * 60)

    print(
        f"TRAINING MODEL: {model_name}"
    )

    # ======================================
    # 14.1 START MLFLOW RUN
    # ======================================

    with mlflow.start_run(
        run_name=model_name
    ) as run:

        # ======================================
        # 14.2 CREATE PIPELINE
        # ======================================

        pipeline = Pipeline([

            (
                "preprocessor",
                preprocessor
            ),

            (
                "model",
                model
            )
        ])

        # ======================================
        # 14.3 TRAIN MODEL
        # ======================================

        pipeline.fit(
            X_train,
            y_train
        )

        # ======================================
        # 14.4 MAKE PREDICTIONS
        # ======================================

        predictions = pipeline.predict(
            X_test
        )

        # ======================================
        # 14.5 CALCULATE METRICS
        # ======================================

        mae = mean_absolute_error(
            y_test,
            predictions
        )

        rmse = (
            mean_squared_error(
                y_test,
                predictions
            ) ** 0.5
        )

        r2 = r2_score(
            y_test,
            predictions
        )

        print(
            f"MAE  : {mae:.2f}"
        )

        print(
            f"RMSE : {rmse:.2f}"
        )

        print(
            f"R2   : {r2:.4f}"
        )

        # ======================================
        # 14.6 LOG PARAMETERS TO MLFLOW
        # ======================================

        mlflow.log_param(
            "model_name",
            model_name
        )

        mlflow.log_param(
            "dataset_rows",
            len(df)
        )

        mlflow.log_param(
            "train_rows",
            len(X_train)
        )

        mlflow.log_param(
            "test_rows",
            len(X_test)
        )

        # Random Forest Parameters

        if model_name == "random_forest":

            mlflow.log_param(
                "n_estimators",
                200
            )

        # XGBoost Parameters

        if model_name == "xgboost":

            mlflow.log_param(
                "n_estimators",
                200
            )

            mlflow.log_param(
                "learning_rate",
                0.05
            )

            mlflow.log_param(
                "max_depth",
                6
            )

        # ======================================
        # 14.7 LOG METRICS TO MLFLOW
        # ======================================

        mlflow.log_metric(
            "mae",
            float(mae)
        )

        mlflow.log_metric(
            "rmse",
            float(rmse)
        )

        mlflow.log_metric(
            "r2",
            float(r2)
        )

        # ======================================
        # 14.8 SAVE TEMP MODEL
        # ======================================

        temp_model_path = (
            f"tmp_mlflow/{model_name}.pkl"
        )

        save_model(
            pipeline,
            temp_model_path
        )

        # ======================================
        # 14.9 LOG ARTIFACTS TO MLFLOW
        # ======================================

        mlflow.log_artifact(
            temp_model_path,
            artifact_path="models"
        )

        mlflow.log_artifact(
            DATASET_PATH,
            artifact_path="datasets"
        )

        # ======================================
        # 14.10 BEST MODEL SELECTION
        # ======================================

        if r2 > best_r2:

            best_r2 = r2

            best_mae = mae

            best_rmse = rmse

            best_model = pipeline

            best_model_name = model_name

            best_run_id = run.info.run_id

            print(
                f"New Best Model: {best_model_name}"
            )

            print(
                f"Best R2 Score: {best_r2:.4f}"
            )


# ======================================
# SECTION 15
# SAVE BEST MODEL
# ======================================

print("\n" + "=" * 60)

print(
    "SAVING BEST MODEL"
)

print("=" * 60)

model_output_path = (

    f"trained_models/"

    f"{best_model_name}_model.pkl"
)


save_model(
    best_model,
    model_output_path
)


save_model(
    best_model,
    CURRENT_MODEL_PATH
)


print(
    f"Best Model Name : {best_model_name}"
)

print(
    f"Model Saved     : {model_output_path}"
)

print(
    f"Current Model   : {CURRENT_MODEL_PATH}"
)

print(
    f"Best Run ID     : {best_run_id}"
)

print(
    f"Best R2 Score   : {best_r2:.4f}"
)

print(
    f"Best MAE        : {best_mae:.2f}"
)

print(
    f"Best RMSE       : {best_rmse:.2f}"
)


# ======================================
# SECTION 16
# UPLOAD ARTIFACTS TO MINIO
# ======================================

print("\n" + "=" * 60)

print(
    "UPLOADING ARTIFACTS TO MINIO"
)

print("=" * 60)

timestamp = datetime.now().strftime(
    "%Y%m%d_%H%M%S"
)

# ======================================
# UPLOAD CURRENT MODEL
# ======================================

s3_client.upload_file(

    CURRENT_MODEL_PATH,

    BUCKET_NAME,

    "current/current_model.pkl"
)

print(
    "Current model uploaded successfully."
)

# ======================================
# UPLOAD VERSIONED MODEL
# ======================================

versioned_model = (
    f"versions/model_{timestamp}.pkl"
)

s3_client.upload_file(

    CURRENT_MODEL_PATH,

    BUCKET_NAME,

    versioned_model
)

print(
    f"Versioned model uploaded: {versioned_model}"
)

# ======================================
# UPLOAD TRAINING DATASET
# ======================================

s3_client.upload_file(

    DATASET_PATH,

    BUCKET_NAME,

    "datasets/retraining_dataset.csv"
)

print(
    "Training dataset uploaded successfully."
)

# ======================================
# UPLOAD MODEL METADATA
# ======================================

metadata_file = (
    "trained_models/model_metadata.txt"
)

with open(
    metadata_file,
    "w"
) as file:

    file.write(
        f"Model Name : {best_model_name}\n"
    )

    file.write(
        f"Run ID : {best_run_id}\n"
    )

    file.write(
        f"R2 Score : {best_r2:.4f}\n"
    )

    file.write(
        f"MAE : {best_mae:.2f}\n"
    )

    file.write(
        f"RMSE : {best_rmse:.2f}\n"
    )

    file.write(
        f"Created At : {timestamp}\n"
    )

s3_client.upload_file(

    metadata_file,

    BUCKET_NAME,

    "metadata/model_metadata.txt"
)

print(
    "Model metadata uploaded successfully."
)

print(
    "\nMinIO Upload Completed Successfully"
)


# ======================================
# SECTION 17
# SUMMARY
# ======================================

print("\n")

print("=" * 60)

print(
    "TRAINING COMPLETED SUCCESSFULLY"
)

print("=" * 60)

print(
    f"Best Model      : {best_model_name}"
)

print(
    f"Best Run ID     : {best_run_id}"
)

print(
    f"R2 Score        : {best_r2:.4f}"
)

print(
    f"MAE             : {best_mae:.2f}"
)

print(
    f"RMSE            : {best_rmse:.2f}"
)

print(
    f"Local Model     : {CURRENT_MODEL_PATH}"
)

print(
    f"Dataset         : {DATASET_PATH}"
)

print(
    f"MinIO Bucket    : {BUCKET_NAME}"
)

print(
    f"MLflow Server   : {MLFLOW_URI}"
)

print("=" * 60)

print(
    "ARTIFACTS STORED"
)

print("=" * 60)

print(
    "✓ MLflow Metrics"
)

print(
    "✓ MLflow Parameters"
)

print(
    "✓ MLflow Artifacts"
)

print(
    "✓ MinIO Current Model"
)

print(
    "✓ MinIO Versioned Model"
)

print(
    "✓ MinIO Training Dataset"
)

print(
    "✓ MinIO Metadata"
)

print("=" * 60)

print(
    "MODEL READY FOR PREDICTION API"
)

print("=" * 60)

print("\n")



