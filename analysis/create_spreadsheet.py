import json
import pandas as pd


products = []
with open("products.json", mode="r") as file:
    results = json.loads(file.read())["results"]
    for product in results:
        products.append(product)


product_data = pd.DataFrame(products)

product_data.to_excel("products.xlsx", sheet_name="produtos", index=False)
