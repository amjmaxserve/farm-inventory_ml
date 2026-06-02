from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.models import (
    User,
    ModelRegistry
)

from app.database.dependencies import get_db

from app.schemas.model_registry_schema import (
    ModelRegistryCreate,
    ModelRegistryResponse,
)

from app.auth.dependencies import require_data_scientist
from app.database.models import (
    User,
    ModelRegistry,
    AuditLog
)

router = APIRouter(
    prefix="/models",
    tags=["Model Registry"]
)


@router.get(
    "/",
    response_model=list[ModelRegistryResponse]
)
def list_models(
    db: Session = Depends(get_db)
):
    return (
        db.query(ModelRegistry)
        .order_by(ModelRegistry.id.desc())
        .all()
    )


@router.get(
    "/current",
    response_model=ModelRegistryResponse
)
def current_model(
    db: Session = Depends(get_db)
):
    model = (
        db.query(ModelRegistry)
        .filter(
            ModelRegistry.status == "PRODUCTION"
        )
        .first()
    )

    if not model:
        raise HTTPException(
            status_code=404,
            detail="No production model found"
        )

    return model


@router.post(
    "/",
    response_model=ModelRegistryResponse
)
def register_model(
    model: ModelRegistryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_data_scientist),
):
    existing_model = (
        db.query(ModelRegistry)
        .filter(
            ModelRegistry.version == model.version
        )
        .first()
    )

    if existing_model:
        raise HTTPException(
            status_code=400,
            detail="Model version already exists"
        )

    existing_production = (
        db.query(ModelRegistry)
        .filter(
            ModelRegistry.status == "PRODUCTION"
        )
        .first()
    )
    
    status  = (
        "PRODUCTION"
        if existing_production is None
        else "STAGING"
    )
    db_model = ModelRegistry(
        model_name=model.model_name,
        version=model.version,
        mlflow_run_id=model.mlflow_run_id,
        artifact_path=model.artifact_path,
        accuracy=model.accuracy,
        status=status,
    )

    db.add(db_model)
    db.commit()
    db.refresh(db_model)

    return db_model


@router.post(
    "/promote/{version}",
    response_model=ModelRegistryResponse
)
def promote_model(

    version: str,

    db: Session = Depends(get_db),

    current_user: User = Depends(
        require_data_scientist
    )
):

    target_model = (
        db.query(ModelRegistry)
        .filter(
            ModelRegistry.version == version
        )
        .first()
    )

    if not target_model:

        raise HTTPException(
            status_code=404,
            detail="Model version not found"
        )

    (
        db.query(ModelRegistry)
        .filter(
            ModelRegistry.status == "PRODUCTION"
        )
        .update(
            {"status": "STAGING"}
        )
    )

    target_model.status = "PRODUCTION"
    
    audit_log = AuditLog(
        username=current_user.username,
        action="PROMOTE_MODEL",
        resource="MODEL_REGISTRY",
        details=f"Promoted model version {version} to PRODUCTION"
    )

    db.add(audit_log)
    db.commit()

    db.refresh(target_model)

    return target_model