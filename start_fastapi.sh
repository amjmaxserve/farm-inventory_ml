#!/bin/sh

echo "=================================="
echo "EXPORTING TRAINING DATASET"
echo "=================================="

python -m scripts.export_training_dataset

echo "=================================="
echo "RETRAINING MODEL"
echo "=================================="

python -m app.ml.retrain_model

echo "=================================="
echo "STARTING FASTAPI"
echo "=================================="

uvicorn main:app --host 0.0.0.0 --port 8000
