


import os
import src.KeycrmOpenApi as KeycrmOpenApi


def main():



    order_id = 71588


    BUNDLE_CUSTOM_FIELD_ID = os.getenv("BUNDLE_CUSTOM_FIELD_ID")

    order_data = KeycrmOpenApi.get_order_data(order_id)

    order_products = order_data['products']

    bundles = []

    for product in order_products:
        if "[bundle]" in product.name:
            bundles.append(product)

    
    for bundle in bundles:

        bundle_data = KeycrmOpenApi.get_product_data_by_id(bundle["product_id"])

        bundle_custom_field = bundle_data[BUNDLE_CUSTOM_FIELD_ID]

        if bundle_custom_field != None:
            

            products_from_bundle_data = KeycrmOpenApi.get_products_data_from_bundle_custom_field(bundle_custom_field)

            products = get_full_products_data_from_bundle_data(products_from_bundle_data)

            KeycrmApi.add_products_to_order(products)

            



            

