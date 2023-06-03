from flask import Flask
import time

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return '<b>' + function() + '</b>'

    return wrapper_function


@app.route("/")
@make_bold
def hello_world():
    return "<p>Hello, World!</p>"


@make_bold
def welcome(stuff):
    return stuff


if __name__ == "__main__":
    app.run(debug=True)
