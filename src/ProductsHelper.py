

class ProductsHelper:


    @staticmethod
    def prepare_products_json(products_data, order_id):
        print(products_data)

        result = {"products": []}

        for offer in products_data['data']:
            product = offer["product"]
            sku = offer["sku"]
            quantity = offer["quantity"]

        
            thumbnail = product["thumbnail_url"]

            product_json = {
                "quantity": float(quantity),
                "sku": sku,
                "name": product["name"],
                "price": offer["price"],
                "order_id": order_id,
                "offer_id": offer["id"],
                "product_id": product["id"],
                "purchased_price": offer["purchased_price"],
                "thumbnail_url": thumbnail,
                "picture": {
                    "thumbnail": thumbnail
                },
                "unit_type": product["unit_type"] or "шт"
            }

            result["products"].append(product_json)

        print(result)
        return result