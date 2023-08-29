from flask import Flask, render_template, request
import requests
import datetime as dt
import os
import smtplib

app = Flask(__name__)

@app.route('/')
def home():
    posts = requests.get('https://api.npoint.io/8ae9de22616777ac9a2f').json()
    date = dt.datetime.now().strftime('%B %-d, %Y')
    print(date)
    return render_template('index.html', posts=posts, date=date)

@app.route('/contact', methods=["GET","POST"])
def contact():
    get = request.method
    if get=='GET':
        return render_template('contact.html', request=get)
    else:
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        msg=request.form['message']
        send_email(name,email,phone,msg)
        return render_template('contact.html', request=get)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:id>')
def post(id):
    posts = requests.get('https://api.npoint.io/8ae9de22616777ac9a2f').json()
    date = dt.datetime.now().strftime('%B %-d, %Y')
    return render_template('post.html', post=posts[id-1], date=date)

def send_email(name, email, phone, msg):
    password = os.environ['APP_PASSWORD']
    email = f"Subject: New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {msg}"
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user='pythonchowdhury@gmail.com', password=password)
        connection.sendmail(from_addr='pythonchowdhury@gmail.com',
                            to_addrs='pythonchowdhury@gmail.com',
                            msg='Subject: New Message\n\n' + email)

if __name__ =='__main__':
    app.run(debug=True)