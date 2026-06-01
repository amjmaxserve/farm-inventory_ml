from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def get_admin_token():

    response = client.post(

        "/api/auth/login",

        data={
            "username": "admin",
            "password": "Admin123"
        }
    )

    token = response.json()["access_token"]

    return token