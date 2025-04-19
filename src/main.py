


import os

from KeycrmOpenApi import KeycrmOpenApi
from BundleHelper import BundleHelper
from ProductsHelper import ProductsHelper
from KeycrmApi import KeycrmApi

def main():



    order_id = 71588


    BUNDLE_CUSTOM_FIELD_ID = os.getenv("BUNDLE_CUSTOM_FIELD_ID")

    order_data = KeycrmOpenApi.get_order_data(order_id)

    order_products = order_data['products']

    bundles = []

    for product in order_products:
    
        if "[bundle]" in product["name"]:
            bundles.append(product)


    for bundle in bundles:

    
        bundle_data = KeycrmOpenApi.get_product_data_by_id(bundle["offer"]["product_id"])
       
        bundle_custom_field = next((f["value"] for f in bundle_data["data"][0]["custom_fields"] if f["uuid"] == "CT_1881"), None)
        print(bundle_custom_field)

        if bundle_custom_field != None:
            

            products_from_bundle_data = BundleHelper.get_products_data_from_bundle_custom_field(bundle_custom_field)

            print(products_from_bundle_data[0]["sku"])

            

            skus_and_quantities = {product["sku"]: product["quantity"] for product in products_from_bundle_data}    

            products = KeycrmOpenApi.get_products_data_by_skus_and_quantities(skus_and_quantities)
        
            print("---------------")
            KeycrmApi.add_products_to_order(ProductsHelper.prepare_products_json(products,order_id), order_id)

            print("succesfull add product")

            



            
main() 

