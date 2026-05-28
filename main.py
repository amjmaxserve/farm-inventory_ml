from fastapi import FastAPI

from app.api.predict import router as predict_router
from app.api.inventory import router as inventory_router
from app.api.prediction_history import router as prediction_history_router

app = FastAPI()

app.include_router(predict_router)
app.include_router(prediction_history_router)
app.include_router(inventory_router)


@app.get("/")
def home():

    return {
        "message": "Farm Inventory API Running"
    }