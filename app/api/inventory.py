from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.database.models import Inventory

from app.schemas.inventory_schema import (
    InventoryCreate,
    InventoryResponse
)

from app.database.models import User

from app.auth.dependencies import (
    get_current_user,
    require_admin,
    require_inventory_manager
)

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)


@router.post("/", response_model=InventoryResponse)
def create_inventory(
    inventory: InventoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_inventory_manager)
):

    db_inventory = Inventory(
        item_name=inventory.item_name,
        category=inventory.category,
        crop_type=inventory.crop_type,
        quantity=inventory.quantity,
        unit=inventory.unit,
        minimum_stock_level=inventory.minimum_stock_level,
        cost=inventory.cost,
        supplier=inventory.supplier,
        storage_location=inventory.storage_location,
        expiry_date=inventory.expiry_date,
        batch_number=inventory.batch_number,
        season=inventory.season,
        usage_per_month=inventory.usage_per_month,
        
    )

    db.add(db_inventory)

    db.commit()

    db.refresh(db_inventory)

    return db_inventory


@router.get("/")
def list_inventory(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return db.query(Inventory).all()


@router.delete("/{inventory_id}")
def delete_inventory(
    inventory_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):

    inventory = db.query(Inventory).filter(
        Inventory.id == inventory_id
    ).first()

    if not inventory:

        raise HTTPException(
            status_code=404,
            detail="Inventory not found"
        )

    db.delete(inventory)

    db.commit()

    return {
        "message": "Inventory deleted successfully"
    }