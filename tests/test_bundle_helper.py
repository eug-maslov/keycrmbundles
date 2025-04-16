import pytest

from src.BundleHelper import BundleHelper


def test_get_products_from_custom_field():
   
    data = BundleHelper.get_products_data_from_bundle_custom_field(r'{% sku: "test"; price: 2500; amount: 5; discount: 45 %}, {% sku: "test2"; price: 2500; amount: 5; discount: 45 %}')

    

    assert len(data) == 2
    assert data[0]["sku"] == "test"

