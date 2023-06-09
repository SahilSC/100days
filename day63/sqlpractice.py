from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///new-anime-collection.db'
db = SQLAlchemy()
db.init_app(app)

class Animes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)

def create(title, rating):
    anime = Animes(title=title, rating=rating)
    db.session.add(anime)
    db.session.commit()

def read():
    animelist = db.session.execute(db.select(Animes)).all()

def update(**kwargs):
    query = db.session.execute(db.select(Animes).filter_by(**kwargs)).scalar()
    query.rating = 10
    db.session.commit()

def delete(**kwargs):
    query = db.session.execute(db.select(Animes).filter_by(**kwargs)).scalar()
    db.session.delete(query)
    db.session.commit()

with app.app_context():
    db.create_all()
    delete()
# db = sqlite3.connect('anime-collection.db')
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(50, 'SIJDA', 8.7)")
# db.commit()
