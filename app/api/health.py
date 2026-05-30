from fastapi import APIRouter
from fastapi import HTTPException
from sqlalchemy import text
import requests
import os

from app.database.db import SessionLocal
from app.config import (
    MINIO_HEALTH_URL,
    MLFLOW_HEALTH_URL
)

router = APIRouter()

@router.get("/health")
def health_check():
    
    database_status = "down"
    minio_status = "down"
    mlflow_status = "down"
    model_status = "not loaded"
    
    # ==============================
    # DATABASE CHECK
    # ==============================
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        database_status = "up"
        db.close()
    except Exception:
        pass
    
    # ==============================
    # MINIO CHECK
    # ==============================
    try:
        response = requests.get(MINIO_HEALTH_URL, timeout=5)
        if response.status_code == 200:
            minio_status = "up"
    except Exception:
        pass
    
    # ==============================
    # MLFLOW CHECK
    # ==============================
    try:
        response = requests.get(MLFLOW_HEALTH_URL, timeout=5)
        if response.status_code == 200:
            mlflow_status = "up"
    except Exception:
        pass
    
    # ==============================
    # MODEL CHECK
    # ==============================
    try:
        if os.path.exists(
    "trained_models/current_model.pkl"
):
            model_status = "loaded"
    except Exception:
        pass
    
    # ==============================
    # OVERALL STATUS
    # ==============================
    overall_status = "healthy"
    
    if (
        database_status == "down" or 
        minio_status == "down" or 
        mlflow_status == "down" 
    ):
        overall_status = "unhealthy"
    response = {
        "overall_status": overall_status,
        "database": database_status,
        "minio": minio_status,
        "mlflow": mlflow_status,
        "model": model_status
    }
    
    if overall_status == "unhealthy":
        raise HTTPException(status_code=503, detail=response)
    return response