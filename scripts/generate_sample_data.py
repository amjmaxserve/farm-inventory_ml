import random
from datetime import datetime, timedelta, UTC

from app.database.db import SessionLocal
from app.database.models import (
    Inventory,
    PredictionHistory,
    InventoryUsage
)

db = SessionLocal()

categories = [
    "Seeds",
    "Fertilizers",
    "Pesticides",
    "Tools",
    "Irrigation",
    "Feed"
]

crops = [
    "Rice",
    "Wheat",
    "Corn",
    "Banana",
    "Coconut"
]

seasons = [
    "Summer",
    "Monsoon",
    "Winter"
]

soil_types = [
    "Clay",
    "Sandy",
    "Loamy"
]

locations = [
    "Warehouse A",
    "Warehouse B",
    "Cold Storage",
    "Field Storage"
]

suppliers = [
    "Kerala Agro",
    "FarmTech",
    "GreenLand",
    "Agro India",
    "Agri Corp"
]

# ===================================
# INVENTORY DATA
# ===================================

for i in range(300):

    inventory = Inventory(

        item_name=f"Item-{i}",

        category=random.choice(categories),

        crop_type=random.choice(crops),

        quantity=random.randint(10, 500),

        unit="kg",

        minimum_stock_level=random.randint(20, 80),

        cost=random.randint(1000, 15000),

        supplier=random.choice(suppliers),

        storage_location=random.choice(locations),

        expiry_date="2027-12-31",

        batch_number=f"BATCH-{1000+i}",

        season=random.choice(seasons),

        usage_per_month=random.randint(10, 100)
    )

    db.add(inventory)

db.commit()

print("Inventory data generated")

# ===================================
# PREDICTION HISTORY
# ===================================

for i in range(1000):

    prediction = PredictionHistory(

        crop_type=random.choice(crops),

        season=random.choice(seasons),

        soil_type=random.choice(soil_types),

        rainfall=random.randint(50, 300),

        temperature=random.randint(20, 40),

        humidity=random.randint(40, 95),

        farm_size=random.randint(1, 50),

        previous_usage=random.randint(50, 500),

        predicted_inventory=random.randint(
            100,
            600
        ),

        confidence_score=round(
            random.uniform(0.75, 0.99),
            2
        ),

        model_version="v1",

        created_at=datetime.now(UTC)
        -
        timedelta(days=random.randint(0, 365))
    )

    db.add(prediction)

db.commit()

print("Prediction history generated")

# ===================================
# INVENTORY USAGE
# ===================================

for i in range(3000):

    usage = InventoryUsage(

        inventory_id=random.randint(1, 300),

        crop_type=random.choice(crops),

        season=random.choice(seasons),

        used_quantity=random.randint(1, 50),

        field_location=random.choice(locations),

        usage_date=datetime.now(UTC)
        -
        timedelta(days=random.randint(0, 365))
    )

    db.add(usage)

db.commit()

print("Inventory usage generated")

print("Rich sample data generated successfully")
