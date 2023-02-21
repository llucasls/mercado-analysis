import json
import base64
from io import BytesIO

from requests import request, RequestException, HTTPError, ConnectionError
from flask import request as req, render_template
import pandas as pd
from matplotlib.figure import Figure


BASE_URL = "https://api.mercadolibre.com/sites/MLB"


def get_search_term(query_string: str) -> str:
    query_string = query_string.replace("+", " ")
    query_string = query_string.replace("%20", " ")

    return query_string


def graphics():
    query = req.args.get("q")
    if not query:
        return "Parâmetro de busca não fornecido", 400

    product_name = get_search_term(query)

    try:
        product_url = f"{BASE_URL}/search?q={query}"
    except HTTPError:
        return "HTTPError", 500
    except RequestException:
        return "RequestError", 500

    products = []

    try:
        product_response = request("get", product_url)
    except ConnectionError:
        return "Não é possível conectar com o servidor", 500
    product_list = json.loads(product_response.text)

    for product in product_list["results"]:
        products.append(product)

    product_data = pd.DataFrame(products)
    prices = product_data["price"]

    histogram = Figure()
    ax = histogram.subplots()
    ax.hist(prices)
    ax.set_title("Preços do produto em reais")
    buf = BytesIO()
    histogram.savefig(buf, format="png")
    hist_data = base64.b64encode(buf.getbuffer()).decode("ascii")

    boxplot = Figure()
    ax = boxplot.subplots()
    ax.boxplot(prices)
    ax.set_title("Preços do produto em reais")
    buf = BytesIO()
    boxplot.savefig(buf, format="png")
    boxplot_data = base64.b64encode(buf.getbuffer()).decode("ascii")

    return render_template("graphics.jinja",
                           product_name=product_name,
                           hist_data=hist_data,
                           boxplot_data=boxplot_data,
                           mode="light-mode")
