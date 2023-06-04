from flask import Flask
import random

app = Flask(__name__)

randomnumber = random.randint(1,10)

@app.route("/")
def home():
    return "<h1>Guess a number from 1 to 10</h1>" \
           '<img src="https://media.giphy.com/media/qVDmGRCLEX4Z2FpyUX/giphy.gif">'


@app.route("/<guess>")
def guess_number(guess):
    if guess > randomnumber:
        "<h1 "


if __name__ == "__main__":
    app.run(debug="True")