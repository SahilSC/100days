from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import *
from flask_bootstrap import Bootstrap

class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Submit')

app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'Secret'

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST','GET'])
def login():
    loginform = LoginForm()
    if loginform.validate_on_submit():
        if loginform.email.data=='admin@email.com' and loginform.password.data=='12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=loginform)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/testing')
def testing():
    return render_template('testing.html')

if __name__ == '__main__':
    app.run(debug=True)