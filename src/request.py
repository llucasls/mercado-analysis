from requests import request


BASE_URL = "https://api.mercadolibre.com/sites/MLB"
product_url = f"{BASE_URL}/search?q=computador"

product_list = request("get", product_url)


print(product_list)
