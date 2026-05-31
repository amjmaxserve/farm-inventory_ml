from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_inventory_list():

    response = client.get(
        "/api/inventory/"
    )

    assert response.status_code == 200

    assert isinstance(
        response.json(),
        list
    )