from flask import Flask, render_template
import requests
import datetime as dt

app = Flask(__name__)

@app.route('/')
def home():
    posts = requests.get('https://api.npoint.io/8ae9de22616777ac9a2f').json()
    date = dt.datetime.now().strftime('%B %-d, %Y')
    print(date)
    return render_template('index.html', posts=posts, date=date)

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/post/<int:id>')
def post(id):
    posts = requests.get('https://api.npoint.io/8ae9de22616777ac9a2f').json()
    date = dt.datetime.now().strftime('%B %-d, %Y')
    return render_template('post.html', post=posts[id-1], date=date)

if __name__ =='__main__':
    app.run(debug=True)