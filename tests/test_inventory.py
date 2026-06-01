from tests.auth_helper import (
    get_admin_token
)


def test_inventory_list(
    client,
    auth_headers
):

    response = client.get(
        "/api/inventory/",
        headers=auth_headers
    )

    assert response.status_code == 200

