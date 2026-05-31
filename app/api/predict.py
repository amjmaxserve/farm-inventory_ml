
from fastapi import APIRouter
from fastapi import Depends

import pandas as pd
import joblib

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.database.models import (
    PredictionHistory,
    Inventory
)

from app.ml.model_loader import download_latest_model


# ==========================================
# LOAD MODEL FROM MINIO
# ==========================================

model = None

def get_model():
    
    global model

    if model is None:
        model = download_latest_model()

    return model
router = APIRouter()



# ==========================================
# PREDICTION API
# ==========================================

@router.post("/predict")
def predict_inventory(

    crop_type: str,

    season: str,

    soil_type: str,

    rainfall: float,

    temperature: float,

    humidity: float,

    farm_size: float,

    previous_usage: float,

    db: Session = Depends(get_db)
):

    # ======================================
    # CREATE INPUT DATAFRAME
    # ======================================

    input_df = pd.DataFrame([{

        "crop_type": crop_type,

        "season": season,

        "soil_type": soil_type,

        "rainfall": rainfall,

        "temperature": temperature,

        "humidity": humidity,

        "farm_size": farm_size,

        "previous_usage": previous_usage
    }])

    # ======================================
    # MODEL PREDICTION
    # ======================================

    loaded_model = get_model()
    prediction = loaded_model.predict(input_df)[0]

    predicted_value = round(
        float(prediction),
        2
    )
    
    # ======================================
    # CURRENT STOCK FOR CROP
    # ======================================
    
    inventory_item = (db.query(Inventory).filter(
        Inventory.crop_type == crop_type
    ).all()
    )
    
    current_stock = sum([item.quantity for item in inventory_item])
    
    # ======================================
    # PURCHASE RECOMMENDATION
    # ======================================
    
    recommended_purchase = max(0, round(predicted_value - current_stock), 2)
    
    if recommended_purchase == 0:
        stock_status = "Sufficient stock available. No purchase needed."
    else:
        stock_status = f"Recommended purchase quantity: {recommended_purchase} units."

    # ======================================
    # SAVE PREDICTION HISTORY
    # ======================================

    history = PredictionHistory(

        crop_type=crop_type,

        season=season,

        soil_type=soil_type,

        rainfall=rainfall,

        temperature=temperature,

        humidity=humidity,

        farm_size=farm_size,

        previous_usage=previous_usage,

        predicted_inventory=predicted_value,

        confidence_score=0.95,

        model_version="xgboost_v1"
    )

    db.add(history)

    db.commit()

    # ======================================
    # RESPONSE
    # ======================================

    return {

        "model": "xgboost_v1",

        "predicted_inventory": predicted_value,
        
        "current_stock": current_stock,
        
        "recommended_purchase": recommended_purchase,
        
        "stock_status": stock_status,

        "confidence_score": 0.95
    }

