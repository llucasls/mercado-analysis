from flask import Flask

from src.views.home import home
from src.views.graphics import graphics


app = Flask("mercado_analysis")


app.route("/")(home)
app.route("/graphics/")(graphics)
