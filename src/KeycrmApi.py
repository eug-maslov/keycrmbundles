import os
import requests
from dotenv import load_dotenv, set_key, find_dotenv

class KeycrmApi:
    load_dotenv()

    API_KEY = os.getenv("MANAGER_KEY")
    CRM_NAME = os.getenv("CRM_NAME")
    CRM_LOGIN = os.getenv("LOGIN")
    CRM_PASSWORD = os.getenv("PASSWORD")

    @classmethod
    def add_products_to_order(cls, products_data, order_id):
        attempt = 0

        while attempt < 3:
            response = requests.post(
                f"https://{cls.CRM_NAME}.api.keycrm.app/orders/{order_id}/products",
                headers={"authorization": f"Bearer {cls.API_KEY}"},
                json=products_data
            )

            if response.status_code == 401:
                attempt += 1
                print(f"Attempt {attempt}: Unauthorized. Refreshing token...")
                cls.update_manager_key_env()
            elif response.status_code in [200, 201]:
                return response.json()
            else:
                raise Exception(f"Error {response.status_code}: {response.text}")

        raise Exception("Failed after 3 attempts: Unauthorized (401)")


    @classmethod
    def update_manager_key_env(cls):
        login_url = f"https://{cls.CRM_NAME}.api.keycrm.app/auth/login"
        payload = {
            "username": cls.CRM_LOGIN,
            "password": cls.CRM_PASSWORD
        }

        headers = {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "origin": f"https://{cls.CRM_NAME}.keycrm.app",
            "referer": f"https://{cls.CRM_NAME}.keycrm.app/",
            "authorization": "Bearer null"
        }

        response = requests.post(login_url, headers=headers, json=payload)
        if response.status_code == 200:
            new_token = response.json().get("access_token")
            if not new_token:
                raise Exception("Login successful but token not found in response.")

            cls.API_KEY = new_token
            os.environ["MANAGER_KEY"] = new_token 

        
            dotenv_path = find_dotenv()
            if dotenv_path:
                set_key(dotenv_path, "MANAGER_KEY", new_token)
                print("Token refreshed and saved to .env.")
            else:
                print("Warning: .env file not found, cannot update token persistently.")
        else:
            raise Exception(f"Failed to update API key: {response.status_code} - {response.text}")

