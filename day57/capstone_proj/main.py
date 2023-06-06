from flask import Flask, render_template
import requests
#day 57

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391').json()
    return render_template("index.html", posts=response)

@app.route('/post/<int:id>')
def post(id):
    response = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391').json()[id-1]
    body = response['body']
    subtitle = response['subtitle']
    title=response['title']
    return render_template('post.html', body=body,subtitle=subtitle,title=title)

if __name__ == "__main__":
    app.run(debug=True)
