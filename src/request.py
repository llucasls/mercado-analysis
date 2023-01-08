import json
from requests import request


BASE_URL = "https://api.mercadolibre.com/sites/MLB"
product_url = f"{BASE_URL}/search?q=computador"

product_response = request("get", product_url)
product_list = json.loads(product_response.text)


print(product_list)


with open("products.json", mode="w") as file:
    file.write(product_response.text)
