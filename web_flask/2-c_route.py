#!/usr/bin/python3
"""Flask app """


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_text(text):
    text = text.replace("_", " ")
    return f"C {text}"


if "__main__" == __name__:
    app.run(port=5000, host="0.0.0.0")
