

from flask import Flask, render_template

app = Flask(__name__)

app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("main_page.html")


@app.route("/projects/")
def projects():
    return render_template("project_page.html")

@app.route("/test/")
def test():
    return render_template("test.html")

