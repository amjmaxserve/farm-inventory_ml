def test_prediction(
    client,
    auth_headers
):

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
        },

        headers=auth_headers
    )

    assert response.status_code == 200