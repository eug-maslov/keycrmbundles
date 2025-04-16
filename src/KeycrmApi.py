
import os
from dotenv import load_dotenv
import requests

class KeycrmHiddenApi:
    load_dotenv()


    API_KEY = os.getenv("MANAGER_KEY")


    @classmethod
    def add_products_to_order(products_data):
