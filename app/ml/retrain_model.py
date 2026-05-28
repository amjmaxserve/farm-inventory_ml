
import pandas as pd
import joblib

from sklearn.compose import ColumnTransformer

from sklearn.pipeline import Pipeline

from sklearn.preprocessing import OneHotEncoder

from sklearn.impute import SimpleImputer

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from xgboost import XGBRegressor


# ======================================
# LOAD DATASET
# ======================================

DATASET_PATH = "datasets/retraining_dataset.csv"

df = pd.read_csv(DATASET_PATH)

print("\nDataset Loaded Successfully\n")

print(df.head())

print("\nDataset Shape:", df.shape)


# ======================================
# FEATURES & TARGET
# ======================================

X = df[[
    "crop_type",
    "season",
    "soil_type",
    "rainfall",
    "temperature",
    "humidity",
    "farm_size",
    "previous_usage"
]]

Y = df["predicted_inventory"]


# ======================================
# COLUMN TYPES
# ======================================

categorical_columns = [
    "crop_type",
    "season",
    "soil_type"
]

numerical_columns = [
    "rainfall",
    "temperature",
    "humidity",
    "farm_size",
    "previous_usage"
]


# ======================================
# PREPROCESSING PIPELINES
# ======================================

categorical_transformer = Pipeline([
    (
        "imputer",
        SimpleImputer(
            strategy="most_frequent"
        )
    ),
    (
        "encoder",
        OneHotEncoder(
            handle_unknown="ignore"
        )
    )
])

numerical_transformer = Pipeline([
    (
        "imputer",
        SimpleImputer(
            strategy="median"
        )
    )
])


# ======================================
# COLUMN TRANSFORMER
# ======================================

preprocessor = ColumnTransformer([
    (
        "cat",
        categorical_transformer,
        categorical_columns
    ),
    (
        "num",
        numerical_transformer,
        numerical_columns
    )
])


# ======================================
# TRAIN TEST SPLIT
# ======================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)


# ======================================
# MODELS
# ======================================

models = {

    "random_forest": RandomForestRegressor(
        n_estimators=200,
        random_state=42
    ),

    "xgboost": XGBRegressor(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=6,
        random_state=42
    )
}


# ======================================
# TRAINING LOOP
# ======================================

best_model = None

best_model_name = None

best_r2 = -999


for model_name, model in models.items():

    print("\n" + "=" * 60)

    print(f"TRAINING MODEL: {model_name}")

    pipeline = Pipeline([
        (
            "preprocessor",
            preprocessor
        ),
        (
            "model",
            model
        )
    ])

    pipeline.fit(
        X_train,
        y_train
    )

    predictions = pipeline.predict(X_test)

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    rmse = (
        mean_squared_error(
            y_test,
            predictions
        ) ** 0.5
    )

    r2 = r2_score(
        y_test,
        predictions
    )

    print(f"MAE  : {mae:.2f}")

    print(f"RMSE : {rmse:.2f}")

    print(f"R2   : {r2:.4f}")

    if r2 > best_r2:

        best_r2 = r2

        best_model = pipeline

        best_model_name = model_name


# ======================================
# SAVE BEST MODEL
# ======================================

model_output_path = (
    f"trained_models/"
    f"{best_model_name}_model.pkl"
)

joblib.dump(
    best_model,
    model_output_path
)


joblib.dump(
    best_model,
    "trained_models/current_model.pkl"
)

print("\n" + "=" * 60)

print("BEST MODEL SELECTED")

print(f"Model Name : {best_model_name}")

print(f"Best R2    : {best_r2:.4f}")

print(f"Model Saved: {model_output_path}")

print("=" * 60)
