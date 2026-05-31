
from pydantic import BaseModel
from typing import Optional
from pydantic import ConfigDict




class InventoryCreate(BaseModel):

    item_name: str

    category: str

    crop_type: Optional[str] = None

    quantity: float

    unit: str

    minimum_stock_level: Optional[float] = 50

    cost: Optional[float] = None

    supplier: Optional[str] = None

    storage_location: Optional[str] = None

    expiry_date: Optional[str] = None

    batch_number: Optional[str] = None

    season: Optional[str] = None

    usage_per_month: Optional[float] = None


class InventoryResponse(InventoryCreate):

    id: int

    model_config = ConfigDict(from_attributes=True)
