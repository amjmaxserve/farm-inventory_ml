import pandas as pd

from app.database.db import SessionLocal
from app.database.models import PredictionHistory


db = SessionLocal()

records = db.query(PredictionHistory).all()

rows = []

for item in records:

    rows.append({
        "crop_type": item.crop_type,
        "season": item.season,
        "soil_type": item.soil_type,
        "rainfall": item.rainfall,
        "temperature": item.temperature,
        "humidity": item.humidity,
        "farm_size": item.farm_size,
        "previous_usage": item.previous_usage,
        "predicted_inventory": item.predicted_inventory
    })


df = pd.DataFrame(rows)

output_path = "datasets/retraining_dataset.csv"


df.to_csv(output_path, index=False)

print(f"Dataset exported successfully -> {output_path}")