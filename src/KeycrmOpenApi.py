


import os
from dotenv import load_dotenv
import requests

class KeycrmOpenApi:
    load_dotenv()

    BASE_URL = "https://openapi.keycrm.app/v1"

    API_KEY = os.getenv("OPEN_API_KEY")

    @classmethod
    def get_headers(cls):
        return {"Authorization": f"Bearer {cls.API_KEY}"}

    @classmethod
    def get_order_data(cls, order_id):
  
        response = requests.get(f"{cls.BASE_URL}/order/{order_id}?include=products.offer", headers=cls.get_headers())
        
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.text}")
        
      
        return response.json()
    

    
    @classmethod
    def get_product_data_by_id(cls, product_id):

        response = requests.get(f"{cls.BASE_URL}/products?filter[product_id]={product_id}&include=custom_fields", headers=cls.get_headers())
        
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.text}")
        
      
        return response.json() 
    

    @classmethod 
    def get_products_data_by_skus_and_quantities(cls, products_skus_and_quantities):
      
      
        products_skus_string = ",".join(products_skus_and_quantities.keys())

        print(products_skus_string)

        response = requests.get(f"{cls.BASE_URL}/offers?filter[sku]={products_skus_string}&include=product&limit=50", headers=cls.get_headers())
        
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.text}")
        
      
        response_data = response.json() 

        for product in response_data["data"]:
            sku = product["sku"]
            if sku in products_skus_and_quantities:
                product["quantity"] = products_skus_and_quantities[sku]

        return response_data

  