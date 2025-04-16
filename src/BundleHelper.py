


import csv
from io import StringIO
import re

class BundleHelper:
    
    @staticmethod
    def get_products_data_from_bundle_custom_field(bundle_custom_field):


        blocks = re.findall(r'{%\s*(.*?)\s*%}', bundle_custom_field, re.DOTALL)
        products = []

        for block in blocks:
        
            reader = csv.reader(StringIO(block), delimiter=';')
            parsed_line = next(reader)

            product = {}
            for item in parsed_line:
                if ':' not in item:
                    continue
                key, value = item.strip().split(':', 1)
                key = key.strip()
                value = value.strip().strip('"')  
                product[key] = value
            products.append(product)

        
        return products