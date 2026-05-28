from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.database.models import PredictionHistory

router = APIRouter(
    prefix="/prediction-history",
    tags=["Prediction History"]
)


@router.get("/")
def get_prediction_history(
    db: Session = Depends(get_db)
):

    return db.query(
        PredictionHistory
    ).all()
