


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
    

