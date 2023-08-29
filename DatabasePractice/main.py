from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///anime-collection.db'
db = SQLAlchemy()
db.init_app(app)


class Anime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    rating=db.Column(db.Float, nullable=False)


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method=='POST':
        if 'addbutton' in request.form:
            create(request.form['name'],request.form['rating'])
        elif 'ratingbutton' in request.form:
            update_anime_rating(request.form['id'], request.form['rating'])

    anime_list = list_animes()
    return render_template('index.html', anime_list=anime_list)

@app.route('/edit')
def edit_rating():
    return render_template('edit.html', anime=get_anime(int(request.args.get('id',''))))

def update_anime_rating(id, rating):
    db.session.execute(db.select(Anime).filter_by(id=id)).scalar().rating = request.form['rating']
    db.session.commit()

@app.route('/delete_anime', methods=['POST'])
def delete_anime():
    db.session.delete(get_anime(request.args.get('id','')))
    db.session.commit()
    return redirect('/')

def create(title, rating):
    db.session.add(Anime(title=title,rating=rating))
    db.session.commit()

def get_anime(id):
    return db.session.execute(db.select(Anime).filter_by(id=id)).scalar()

def list_animes():
    animelist = db.session.execute(db.select(Anime)).all()
    return animelist

@app.route("/add")
def add():
    return render_template('add.html')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
