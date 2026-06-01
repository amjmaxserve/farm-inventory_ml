from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import (get_db)
from app.database.models import PredictionHistory

from app.database.models import User

from app.auth.dependencies import (
    require_ml_access
)

router = APIRouter(
    prefix="/prediction-history",
    tags=["Prediction History"]
)


@router.get("/")
def get_prediction_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_ml_access)
):

    return db.query(
        PredictionHistory
    ).all()
