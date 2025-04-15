import pytest

from src.KeycrmOpenApi import KeycrmOpenApi


def test_get_order_data_success():

    order_id = 71586
    data = KeycrmOpenApi.get_order_data(order_id)

    print(data)
    assert data["id"] == 71586
    assert data["grand_total"] == 988.0
    assert len(data["products"]) == 1