#!/usr/bin/python3
"""Flask app """


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


if "__main__" == __name__:
    app.run(port=5000, host="0.0.0.0")
