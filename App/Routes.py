from App import app
from flask import render_template
@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/form")
def form_page():
    return render_template("form.html")