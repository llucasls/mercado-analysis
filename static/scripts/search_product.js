const URL = "http://127.0.0.1:5000"

function searchProduct(event) {
  const { target } = event;
  const query = target.previousElementSibling.value;

  window.location = `${URL}/graphics?q=${query}`;
}

const button = document.getElementById("search-button");
button.onclick = searchProduct;
