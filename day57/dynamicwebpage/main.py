from flask import Flask, render_template
import requests
import datetime as dt

app = Flask(__name__)

@app.route("/")
def home():
    year = dt.datetime.now().year
    return render_template('index.html', year=year)

@app.route('/blog')
def blog():
    posts = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391').json()
    return render_template('blogpost.html', posts=posts)
@app.route("/guess/<name>")
def guess(name):
    responseage = requests.get(url='https://api.agify.io', params={'name':name}).json()["age"]
    responsegender = requests.get(url='https://api.genderize.io', params={'name':name}).json()['gender']
    return render_template('guessagegender.html', responseage=responseage, responsegender=responsegender, name=name)

if __name__ == '__main__':
    app.run(debug=True)