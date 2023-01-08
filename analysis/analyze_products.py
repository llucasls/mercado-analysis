import json
import pandas as pd
import matplotlib.pyplot as plt


products = []
with open("products.json", mode="r") as file:
    results = json.loads(file.read())["results"]
    for product in results:
        products.append(product)


product_data = pd.DataFrame(products)
prices = product_data["price"]

prices.hist()
plt.show()
