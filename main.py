from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.predict import router as predict_router
from app.api.inventory import router as inventory_router
from app.api.prediction_history import router as prediction_history_router
from app.core.logger import get_logger
from app.api.auth import router as auth_router
from app.api.users import router as users_router
import time


logger = get_logger("fastapi")
app = FastAPI()

@app.middleware("http")
async def log_requests(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = round(time.time() - start_time, 3)
    logger.info(
        f"{request.method} "
        f"{request.url.path} "
        f"{response.status_code} "
        f"{duration}s"
    )
    return response


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

app.include_router(
    auth_router,
    prefix="/api",
    tags=["Authentication"]
)

app.include_router(
    users_router,
    prefix="/api",
    tags=["Users"]
)

@app.get("/")
def home():

    return {
        "message": "Farm Inventory API Running"
    }