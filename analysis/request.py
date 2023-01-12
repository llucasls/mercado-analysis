import sys
import json

from requests import request


def parse_query(user_query: str) -> str:
    return user_query.replace(" ", "+")


BASE_URL = "https://api.mercadolibre.com/sites/MLB"
with open("/dev/tty", "w") as tty:
    tty.write("Por favor, digite o produto da busca: ")
query = input()
query = parse_query(query)


product_url = f"{BASE_URL}/search?q={query}"
product_response = request("get", product_url)


if sys.stdout.isatty():
    print(product_response.text)
else:
    sys.stdout.write(product_response.text)
