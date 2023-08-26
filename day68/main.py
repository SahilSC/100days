from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = "SECRET_KEY_HERE"
app.config['UPLOAD_FOLDER'] = "static/files"
# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(300))
    name = db.Column(db.String(1000))


 
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).filter_by(id=user_id).one()

@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        hashed_password = generate_password_hash(request.form['password'])
        user = User(id=db.session.query(User.id).count()+1,
                    email=request.form['email'],
                    password=hashed_password,
                    name=request.form['name'])
        db.session.add(user)
        db.session.commit()
        # session['name']= request.form['name']
        login_user(user)
        return redirect(url_for('secrets'))
        
    return render_template("register.html", logged_in = current_user.is_authenticated)


@app.route('/login', methods = ["POST", "GET"])
def login():
    if request.method=="POST":
        email = request.form['email']
        password = request.form['password']
        try:
            cur_user = db.session.query(User).filter_by(email=email).one()
        except:
             return redirect(url_for('login'))
        hashed_pass = cur_user.password
        if check_password_hash(hashed_pass, password):
            login_user(cur_user)
            return redirect(url_for('secrets'))
        else:
            flash("Wrong password, try again.")
            return redirect(url_for('login')) #TODO need to redirect w error message back to login
    return render_template("login.html")

@app.route('/secrets', methods=["GET", "POST"])
@login_required
def secrets():
    name=current_user.name
    return render_template("secrets.html", name = name, logged_in = True)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("index.html"))

@app.route('/download')
@login_required
def download():
    return send_from_directory(app.config['UPLOAD_FOLDER'],"cheat_sheet.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
