import datetime

from pydantic import BaseModel, ConfigDict


class ModelRegistryCreate(BaseModel):
    model_name: str
    version: str
    mlflow_run_id: str
    artifact_path: str
    accuracy: float


class ModelRegistryResponse(BaseModel):
    id: int
    model_name: str
    version: str
    mlflow_run_id: str | None = None
    artifact_path: str | None = None
    accuracy: float | None = None
    status: str
    created_at: datetime.datetime | None = None

    model_config = ConfigDict(from_attributes=True)

