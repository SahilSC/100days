from flask import Flask
import random

app = Flask(__name__)

random = random.randint(1,10)

@app.route("/")
def home():
    return "<h1>Guess a number from 1 to 10</h1>" \
           "<img src='https://media.giphy.com/media/qVDmGRCLEX4Z2FpyUX/giphy.gif'>"

@app.route("/<int:guess>")
def guess_number(guess):
    if guess < random:
        return "<h1 style='color:red'>Too low!</h1>" \
               "<img src='https://media.giphy.com/media/l4KibK3JwaVo0CjDO/giphy.gif'>"
    elif guess > random:
        return "<h1 style='color:high'>Too high!</h1>" \
               "<img src='https://media.giphy.com/media/YNPjwaQdIb3K8/giphy.gif'>"
    else:
        return "<h1>CORRECT!!</h1>" \
               "<img src='https://media.giphy.com/media/QvBoMEcQ7DQXK/giphy.gif'>"
    




if __name__ == "__main__":
    app.run(debug="True")