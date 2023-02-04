from flask import render_template

def home():
    return render_template("home.xml", mode="light-mode")
