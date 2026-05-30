
import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://nginx/api"

st.set_page_config(
    page_title="Farm Inventory Dashboard",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 Farm Inventory Management Dashboard")

# ==========================================
# SIDEBAR
# ==========================================

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Dashboard",
        "Inventory",
        "Predictions",
        "Analytics"
    ]
)

# ==========================================
# FETCH DATA
# ==========================================

def get_inventory_data():

    response = requests.get(
        f"{API_URL}/inventory/"
    )

    if response.status_code == 200:

        return response.json()

    return []


def get_prediction_data():

    response = requests.get(
        f"{API_URL}/prediction-history/"
    )

    if response.status_code == 200:

        return response.json()

    return []


inventory_data = get_inventory_data()

prediction_data = get_prediction_data()

inventory_df = pd.DataFrame(inventory_data)

prediction_df = pd.DataFrame(prediction_data)

# ==========================================
# DASHBOARD PAGE
# ==========================================

if menu == "Dashboard":

    st.header("📊 Dashboard Overview")

    total_inventory = len(inventory_df)

    total_predictions = len(prediction_df)

    low_stock_items = pd.DataFrame()

    total_inventory_value = 0

    if not inventory_df.empty:

        low_stock_items = inventory_df[
            inventory_df["quantity"]
            <
            inventory_df["minimum_stock_level"]
        ]

        total_inventory_value = (
            inventory_df["cost"].fillna(0).sum()
        )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Inventory Items",
        total_inventory
    )

    col2.metric(
        "Predictions",
        total_predictions
    )

    col3.metric(
        "Low Stock Alerts",
        len(low_stock_items)
    )

    col4.metric(
        "Inventory Value",
        f"₹ {round(total_inventory_value, 2)}"
    )

    st.markdown("---")

    # ==========================
    # LOW STOCK ALERTS
    # ==========================

    st.subheader("⚠️ Low Stock Alerts")

    if not low_stock_items.empty:

        def highlight_stock(row):

            if row["quantity"] < 20:

                return [
                    "background-color: red"
                ] * len(row)

            elif row["quantity"] < 50:

                return [
                    "background-color: orange"
                ] * len(row)

            return [""] * len(row)

        st.dataframe(
            low_stock_items.style.apply(
                highlight_stock,
                axis=1
            ),
            use_container_width=True
        )

    else:

        st.success("No low stock items")

    st.markdown("---")

    # ==========================
    # RECENT INVENTORY
    # ==========================

    st.subheader("📦 Recent Inventory")

    if not inventory_df.empty:

        st.dataframe(
            inventory_df.head(10),
            use_container_width=True
        )

# ==========================================
# INVENTORY PAGE
# ==========================================

elif menu == "Inventory":

    st.header("📦 Inventory Management")

    st.subheader("Current Inventory")

    if not inventory_df.empty:

        st.dataframe(
            inventory_df,
            use_container_width=True
        )

    else:

        st.warning("No inventory data available")

    st.markdown("---")

    st.subheader("➕ Add Inventory")

    with st.form("inventory_form"):

        col1, col2 = st.columns(2)

        with col1:

            item_name = st.text_input(
                "Item Name"
            )

            category = st.selectbox(
                "Category",
                [
                    "Seeds",
                    "Fertilizers",
                    "Pesticides",
                    "Tools",
                    "Irrigation",
                    "Feed"
                ]
            )

            crop_type = st.selectbox(
                "Crop Type",
                [
                    "Rice",
                    "Wheat",
                    "Corn",
                    "Banana",
                    "Coconut"
                ]
            )

            quantity = st.number_input(
                "Quantity",
                min_value=0.0
            )

            unit = st.text_input(
                "Unit",
                value="kg"
            )

            minimum_stock_level = st.number_input(
                "Minimum Stock Level",
                value=50.0
            )

        with col2:

            cost = st.number_input(
                "Cost",
                min_value=0.0
            )

            supplier = st.text_input(
                "Supplier"
            )

            storage_location = st.selectbox(
                "Storage Location",
                [
                    "Warehouse A",
                    "Warehouse B",
                    "Cold Storage",
                    "Field Storage"
                ]
            )

            expiry_date = st.text_input(
                "Expiry Date",
                value="2027-12-31"
            )

            batch_number = st.text_input(
                "Batch Number"
            )

            season = st.selectbox(
                "Season",
                [
                    "Summer",
                    "Monsoon",
                    "Winter"
                ]
            )

            usage_per_month = st.number_input(
                "Usage Per Month",
                min_value=0.0
            )

        submitted = st.form_submit_button(
            "Add Inventory"
        )

        if submitted:

            payload = {

                "item_name": item_name,

                "category": category,

                "crop_type": crop_type,

                "quantity": quantity,

                "unit": unit,

                "minimum_stock_level":
                    minimum_stock_level,

                "cost": cost,

                "supplier": supplier,

                "storage_location":
                    storage_location,

                "expiry_date": expiry_date,

                "batch_number": batch_number,

                "season": season,

                "usage_per_month":
                    usage_per_month
            }

            response = requests.post(
                f"{API_URL}/inventory/",
                json=payload
            )

            if response.status_code == 200:

                st.success(
                    "Inventory added successfully"
                )

                st.rerun()

            else:

                st.error(
                    "Failed to add inventory"
                )

# ==========================================
# PREDICTIONS PAGE
# ==========================================

elif menu == "Predictions":

    st.header("🤖 Inventory Prediction")

    col1, col2 = st.columns(2)

    with col1:

        crop_type = st.selectbox(
            "Crop Type",
            [
                "Rice",
                "Wheat",
                "Corn",
                "Banana",
                "Coconut"
            ]
        )

        season = st.selectbox(
            "Season",
            [
                "Summer",
                "Monsoon",
                "Winter"
            ]
        )

        soil_type = st.selectbox(
            "Soil Type",
            [
                "Clay",
                "Sandy",
                "Loamy"
            ]
        )

        rainfall = st.number_input(
            "Rainfall"
        )

    with col2:

        temperature = st.number_input(
            "Temperature"
        )

        humidity = st.number_input(
            "Humidity"
        )

        farm_size = st.number_input(
            "Farm Size"
        )

        previous_usage = st.number_input(
            "Previous Usage"
        )

    if st.button("Predict"):

        response = requests.post(
            f"{API_URL}/predict",
            params={

                "crop_type": crop_type,

                "season": season,

                "soil_type": soil_type,

                "rainfall": rainfall,

                "temperature": temperature,

                "humidity": humidity,

                "farm_size": farm_size,

                "previous_usage": previous_usage
            }
        )

        if response.status_code == 200:

            result = response.json()

            st.subheader(
                "Inventory Planning Recommendation"
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Predicted Requirement",
                    f"{result['predicted_inventory']:.2f}"
                )

            with col2:

                st.metric(
                    "Current Stock",
                    f"{result['current_stock']}"
                )

            with col3:

                st.metric(
                    "Recommended Purchase",
                    f"{result['recommended_purchase']}"
                )

            if result["recommended_purchase"] > 0:

                st.warning(
                    result["stock_status"]
                )

            else:

                st.success(
                    result["stock_status"]
                )

            st.caption(
                f"Model: {result['model']} | "
                f"Confidence Score: "
                f"{result['confidence_score']}"
            )

        else:

            st.error(
                "Prediction API failed"
            )

    st.markdown("---")

    st.subheader("📜 Prediction History")

    if not prediction_df.empty:

        st.dataframe(
            prediction_df,
            use_container_width=True
        )

    else:

        st.warning(
            "No prediction history available"
        )

# ==========================================
# ANALYTICS PAGE
# ==========================================

elif menu == "Analytics":

    st.header("📈 Analytics Dashboard")

    if not inventory_df.empty:

        st.subheader(
            "📦 Inventory Distribution"
        )

        category_chart = px.pie(
            inventory_df,
            names="category",
            values="quantity",
            title="Inventory by Category"
        )

        st.plotly_chart(
            category_chart,
            use_container_width=True
        )

        st.subheader(
            "🌾 Crop-wise Inventory"
        )

        crop_chart = px.bar(
            inventory_df,
            x="crop_type",
            y="quantity",
            color="crop_type",
            title="Crop Inventory Analysis"
        )

        st.plotly_chart(
            crop_chart,
            use_container_width=True
        )

        st.subheader(
            "🏭 Supplier Distribution"
        )

        supplier_chart = px.bar(
            inventory_df,
            x="supplier",
            y="cost",
            color="supplier",
            title="Supplier Inventory Value"
        )

        st.plotly_chart(
            supplier_chart,
            use_container_width=True
        )

        st.subheader(
            "📍 Storage Location Distribution"
        )

        location_chart = px.histogram(
            inventory_df,
            x="storage_location",
            color="storage_location",
            title="Storage Distribution"
        )

        st.plotly_chart(
            location_chart,
            use_container_width=True
        )

    if not prediction_df.empty:

        st.subheader(
            "📈 Prediction Trend"
        )

        trend_chart = px.line(
            prediction_df,
            x="created_at",
            y="predicted_inventory",
            color="season",
            title="Prediction Trend"
        )

        st.plotly_chart(
            trend_chart,
            use_container_width=True
        )

        st.subheader(
            "🌧️ Rainfall vs Prediction"
        )

        rainfall_chart = px.scatter(
            prediction_df,
            x="rainfall",
            y="predicted_inventory",
            color="crop_type",
            title="Rainfall Impact"
        )

        st.plotly_chart(
            rainfall_chart,
            use_container_width=True
        )

        st.subheader(
            "🌡️ Temperature vs Prediction"
        )

        temp_chart = px.scatter(
            prediction_df,
            x="temperature",
            y="predicted_inventory",
            color="season",
            title="Temperature Impact"
        )

        st.plotly_chart(
            temp_chart,
            use_container_width=True
        )

        st.subheader(
            "💧 Humidity Analysis"
        )

        humidity_chart = px.box(
            prediction_df,
            x="season",
            y="humidity",
            color="season",
            title="Humidity Distribution"
        )

        st.plotly_chart(
            humidity_chart,
            use_container_width=True
        )

    else:

        st.warning(
            "No analytics data available"
        )