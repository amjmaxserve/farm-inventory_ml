
from fastapi import APIRouter
from fastapi import Depends

import pandas as pd
import joblib

from sqlalchemy.orm import Session

from app.database.dependencies import get_db

from app.database.models import PredictionHistory


router = APIRouter()

# ==========================================
# LOAD TRAINED MODEL
# ==========================================

model = joblib.load(
    "trained_models/current_model.pkl"
)


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

    prediction = model.predict(input_df)

    predicted_value = round(
        float(prediction[0]),
        2
    )

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

        "confidence_score": 0.95
    }

