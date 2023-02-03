def home():
    return """
        <link rel="stylesheet/less" href="/static/style.less" />
        <script src="/static/scripts/less.js"></script>
        <body class="light-mode">
            <header>
                <h1>Mercado Analysis</h1>
                <div>
                    <p>Esta aplicação serve para fazer uma análise estatística
                    de produtos do Mercado Livre.</p>
                    <p>Utilize o campo abaixo para pesquisar preços do produto
                    de sua escolha.</p>
                </div>
            </header>

            <section class="search-field">
                <form>
                    <input type="text" />
                    <button id="search-button" type="button">buscar</button>
                </form>
            </section>
        </body>
        <script src="/static/scripts/search_product.js"></script>
    """
