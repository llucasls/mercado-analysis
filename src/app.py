import json
import base64
from io import BytesIO

from requests import request, RequestException, HTTPError
from flask import Flask, request as req
import pandas as pd
from matplotlib.figure import Figure


app = Flask("mercado_analysis")

BASE_URL = "https://api.mercadolibre.com/sites/MLB"


@app.route("/")
def main():
    return """
        <link rel="stylesheet" href="/static/style.css" />
        <h1>Mercado Analysis</h1>
        <p>Esta aplicação serve para fazer uma análise estatística de produtos
        do Mercado Livre.</p>

        <form>
            <input type="text" />
            <button id="search-button" type="button">buscar</button>
        </form>
        <script src="/static/scripts/search_product.js"></script>
    """

@app.route("/hist/")
def hist():
    query = req.args.get("q")
    if not query:
        return "Parâmetro de busca não fornecido", 400

    try:
        product_url = f"{BASE_URL}/search?q={query}"
    except HTTPError:
        return "HTTPError", 500
    except RequestException:
        return "RequestError", 500

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

    return f"""
        <link rel="stylesheet" href="/static/style.css" />
        <main>
            <img src='data:image/png;base64,{data}' />
        </main>
    """
