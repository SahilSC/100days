from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, FloatField
from wtforms.validators import DataRequired, NumberRange, Length
import requests
import os

endpoint = 'https://api.myanimelist.net/v2'
headers = {
    'X-MAL-CLIENT-ID': os.environ['CLIENT_ID']
}

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///top10animes.db"
db = SQLAlchemy()
db.init_app(app)
Bootstrap(app)


class EditForm(FlaskForm):
    rating = FloatField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired(), NumberRange(min=1, max=10)])
    review = StringField('Your Review', validators=[DataRequired(), Length(max=250)])
    submit = SubmitField('Done')


class AddForm(FlaskForm):
    title = StringField('Anime Title', validators=[DataRequired(), Length(max=250)])
    submit = SubmitField('Add Anime')


class Anime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    year = db.Column(db.Integer)
    description = db.Column(db.String)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    #ranking = db.Column(db.Integer, unique=True)

    review = db.Column(db.String)
    img_url = db.Column(db.String)


sample_anime = Anime(title='Nagi no Asukara',
                     year=2014,
                     description="Due to the closure of their middle school, four students from the sea, Manaka Mukaido, Hikari Sakishima, Chisaki Hiradaira, and Kaname Isaki must attend middle school on the land, despite the growing tension between the land and sea people.",
                     rating=7.9,
                     ranking=1,
                     review="\"Duality of life, romance, faith, and plot twists make this unforgettable.\"",
                     img_url='https://m.media-amazon.com/images/M/MV5BY2RlNzZhYzgtYjMyNi00YTNmLWE5NTktNjdhNTdkYjY4ODg1XkEyXkFqcGdeQXVyNDgyODgxNjE@._V1_.jpg')
sample_movie = Anime(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)


@app.route("/", methods=['POST','GET'])
def home():
    # add_anime_to_sql(sample_movie)
    #add_anime_to_sql(sample_anime)
    animelist = db.session.execute(db.select(Anime).order_by(Anime.rating)).all()
    animelist.reverse()
    print(animelist)
    if animelist:
        for ranking in range(1,len(animelist)+1):
            animelist[ranking-1][0].ranking=ranking
    return render_template("index.html", animelist=animelist)


@app.route('/edit', methods=['GET', 'POST'])
def edit_anime_rating():
    form = EditForm()
    anime = get_anime_sql(request.args.get('id', ''))
    if form.validate_on_submit():
        edit_anime_sql(request.form['animeid'], form.rating.data, form.review.data)
        return redirect(url_for('home'))
    return render_template('edit.html', editform=form, anime=anime)


@app.route('/delete')
def delete_anime():
    delete_anime_from_sql(request.args.get('id', ''))
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add_anime():
    addform = AddForm()
    if addform.validate_on_submit():
        params = {
            'q': addform.title.data,
            'fields': 'title,start_date,synopsis,main_picture,mean'
        }
        animes = [ele['node'] for ele in requests.get(endpoint + "/anime", headers=headers, params=params).json()['data']]
        return render_template('select.html', animes=animes)
        # anime_details = requests.get(endpoint + '/anime/' + str(id), headers=headers, params=params).json()
    return render_template('add.html', form=addform)

@app.route('/select_choice')
def select_choice():
    anime=create_anime(request.args.get('id',''))
    add_anime_to_sql(anime)
    return redirect(url_for('home'))

def delete_anime_from_sql(id):
    db.session.delete(get_anime_sql(id))
    db.session.commit()


def add_anime_to_sql(anime):
    db.session.add(anime)
    db.session.commit()

def create_anime(mal_id):
    anime_details = requests.get(endpoint + '/anime/' + str(mal_id), headers=headers,params={'fields': 'title,start_date,synopsis,main_picture,mean'}).json()
    description=anime_details['synopsis']
    textlen = 543
    if len(description) >= textlen:
        description=description[:textlen-3]+'...'
    anime = Anime(title=anime_details['title'], year=int(anime_details['start_date'][:4]),
                  description=description, rating=anime_details['mean'], ranking=2,
                  review='None', img_url=anime_details['main_picture']['large'])
    return anime

def edit_anime_sql(id, newrating, newreview):
    anime = get_anime_sql(id)
    anime.rating = newrating
    anime.review = newreview
    db.session.commit()


def get_anime_sql(id):
    return db.session.execute(db.select(Anime).filter_by(id=id)).scalar()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
