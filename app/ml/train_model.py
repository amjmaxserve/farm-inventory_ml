import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib


df = pd.read_csv("datasets/inventory_training.csv")

X = df[[
    "rainfall",
    "temperature",
    "farm_size",
    "previous_usage"
]]

Y = df["required_inventory"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

error = mean_absolute_error(y_test, predictions)

print("MAE:", error)

joblib.dump(model, "trained_models/inventory_model.pkl")

print("Model trained successfully")