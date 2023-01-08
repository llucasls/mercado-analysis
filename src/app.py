import json
import base64
from io import BytesIO

from requests import request
from flask import Flask
import pandas as pd
from matplotlib.figure import Figure


app = Flask("mercado_analysis")

BASE_URL = "https://api.mercadolibre.com/sites/MLB"
product_url = f"{BASE_URL}/search?q=memoria+ram+ddr4+8gb"


@app.route("/")
def main():
    return """
        <style>
        html {
            color: navy;
            background-color: aliceblue;
        }
        </style>
        <h1>Mercado Analysis</h1>
        <p>Esta aplicação serve para fazer uma análise estatística de produtos
        do Mercado Livre.</p>
    """


@app.route("/hist/")
def hist():
    products = []

    product_response = request("get", product_url)
    product_list = json.loads(product_response.text)

    for product in product_list["results"]:
        products.append(product)

    product_data = pd.DataFrame(products)
    prices = product_data["price"]

    fig = Figure()
    ax = fig.subplots()
    ax.hist(prices)
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")

    style = """
        <style>
            main {
                display: flex;
                align-items: center;
                justify-content: center;
                flex-direction: column;
            }
        </style>
    """

    content = f"""
        <main>
            <img src='data:image/png;base64,{data}' />
        </main>
    """

    return f"""{style}
               {content}"""
