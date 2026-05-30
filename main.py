from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.predict import router as predict_router
from app.api.inventory import router as inventory_router
from app.api.prediction_history import router as prediction_history_router


app = FastAPI()


app.include_router(
    health_router,
    prefix="/api",
    tags=["Health"]
)

app.include_router(
    predict_router,
    prefix="/api",
    tags=["Prediction"]
)

app.include_router(
    prediction_history_router,
    prefix="/api",
    tags=["Prediction History"]
)

app.include_router(
    inventory_router,
    prefix="/api",
    tags=["Inventory"]
)

@app.get("/")
def home():

    return {
        "message": "Farm Inventory API Running"
    }