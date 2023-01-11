import json
from requests import request


def parse_query(user_query: str) -> str:
    return user_query.replace(" ", "+")


BASE_URL = "https://api.mercadolibre.com/sites/MLB"
query = input("Por favor, digite o produto da busca: ")
query = parse_query(query)


product_url = f"{BASE_URL}/search?q={query}"
product_response = request("get", product_url)


print(product_response.text)
