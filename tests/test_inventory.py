def test_inventory_list(
    client,
    auth_headers
):

    response = client.get(
        "/api/inventory/",
        headers=auth_headers
    )

    assert response.status_code == 200

    assert isinstance(
        response.json(),
        list
    )