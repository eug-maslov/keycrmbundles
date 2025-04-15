import pytest

from src.KeycrmOpenApi import KeycrmOpenApi


def test_get_order_data_success():

    order_id = 71586
    data = KeycrmOpenApi.get_order_data(order_id)

    print(data)
    assert data["id"] == 71586
    assert data["grand_total"] == 988.0
    assert len(data["products"]) == 1


def test_get_product_by_sku():
    product_id = "175689"

    data = KeycrmOpenApi.get_product_data_by_id(product_id)


    assert data['data'][0]['id'] == 175689
