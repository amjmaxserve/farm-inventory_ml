from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_prediction():

    response = client.post(

        "/api/predict",

        params={

            "crop_type": "Rice",

            "season": "Monsoon",

            "soil_type": "Clay",

            "rainfall": 220,

            "temperature": 30,

            "humidity": 75,

            "farm_size": 10,

            "previous_usage": 250
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "predicted_inventory" in data