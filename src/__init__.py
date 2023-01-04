from flask import Flask

app = Flask("mercado_analysis")

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
