from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime
from sqlalchemy import Boolean

from datetime import datetime, UTC

from .db import Base



class Inventory(Base):

    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)

    item_name = Column(String, nullable=False)

    category = Column(String, nullable=False)

    crop_type = Column(String)

    quantity = Column(Float, nullable=False)

    unit = Column(String, nullable=False)

    minimum_stock_level = Column(Float, default=50)

    cost = Column(Float)

    supplier = Column(String)

    storage_location = Column(String)

    expiry_date = Column(String)

    batch_number = Column(String)

    season = Column(String)

    usage_per_month = Column(Float)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC)
    )



class InventoryUsage(Base):

    __tablename__ = "inventory_usage"

    id = Column(Integer, primary_key=True, index=True)

    inventory_id = Column(Integer)

    crop_type = Column(String)

    season = Column(String)

    used_quantity = Column(Float)

    field_location = Column(String)

    usage_date = Column(DateTime)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC)
    )



class PredictionHistory(Base):

    __tablename__ = "prediction_history"

    id = Column(Integer, primary_key=True, index=True)

    crop_type = Column(String)

    season = Column(String)

    soil_type = Column(String)

    rainfall = Column(Float)

    temperature = Column(Float)

    humidity = Column(Float)

    farm_size = Column(Float)

    previous_usage = Column(Float)

    predicted_inventory = Column(Float)

    confidence_score = Column(Float)

    model_version = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC)
    )

class User(Base):
    
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, unique=True, index=True, nullable=False)

    email = Column(String, unique=True, index=True, nullable=False)

    hashed_password = Column(String, nullable=False)
    
    role = Column(String, nullable=False, default="VIEWER")
    
    is_active = Column(Boolean, default=True)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC)
    )
    
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC)
    )


class AuditLog(Base):

    __tablename__ = "audit_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String,
        nullable=False
    )

    action = Column(
        String,
        nullable=False
    )

    resource = Column(
        String,
        nullable=False
    )

    details = Column(
        String
    )

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC)
    )