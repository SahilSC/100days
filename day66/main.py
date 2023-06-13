#api-documentation:https://documenter.getpostman.com/view/27948068/2s93sf2WDW

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random as rd

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/random')
def random():
    coffeelist = get_all_cafes()
    random_cafe = rd.choice(coffeelist)[0]
    dic = random_cafe.__dict__
    return jsonify(dic)


@app.route('/all')
def all():
    coffeelist = get_all_cafes()
    allcafes = {"cafes": []}
    for coffee in coffeelist:
        allcafes['cafes'].append(coffee[0].__dict__)
    return jsonify(allcafes)


@app.route('/search')
def search():
    cafes = {"cafe": []}
    for cafe in get_all_cafes():
        if cafe[0].location == request.args.get('loc', ''):
            cafes['cafe'].append(cafe[0].__dict__)
    if not cafes['cafe']:
        return jsonify(error={'Not Found': "Sorry, we don't have a cafe at that location."})
    return jsonify(cafes)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    map_url =request.form['map_url']
    img_url =request.form['img_url']
    location =request.form['location']
    seats =request.form['seats']
    has_toilet =bool(request.form['has_toilet'])
    has_wifi =bool(request.form['has_wifi'])
    has_sockets =bool(request.form['has_sockets'])
    can_take_calls =bool(request.form['can_take_calls'])
    coffee_price =request.form['coffee_price']
    cafe = Cafe(name=name, map_url=map_url, img_url=img_url,location=location,seats=seats,has_toilet=has_toilet,
                has_wifi=has_wifi,has_sockets=has_sockets,can_take_calls=can_take_calls,coffee_price=coffee_price)
    db.session.add(cafe)
    db.session.commit()
    return jsonify(response={"success": 'Successfully added new cafe.'})

@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    try:
        cafe = db.session.execute(db.select(Cafe).filter_by(id=cafe_id)).scalar()
        cafe.coffee_price = request.args.get('new_price','')
        db.session.commit()
        return jsonify(success="Successfully updated the price.")
    except:
        return jsonify(error={"Not found":"Sorry a cafe with that id was not found in the database."})

@app.route('/report-closed/<int:cafe_id>',methods=['DELETE'])
def delete(cafe_id):
    secret_api_key = 'TopSecretAPIKey'
    if request.args.get('api_key')==None:
        return jsonify(error="Please pass your api key using the api_key parameter.")
    try:
        cafe = db.session.execute(db.select(Cafe).filter_by(id=cafe_id)).scalar()
        if request.args.get('api_key','')==secret_api_key:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(success="Successfully deleted cafe.")
        else:
            return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api_key.")
    except:
        return jsonify(error={"Not Found":"Sorry a cafe with that id was not found in the database."})

def get_all_cafes():
    allcoffee = db.session.execute(db.select(Cafe)).all()
    for coffee in allcoffee:
        del coffee[0].__dict__['_sa_instance_state']
    return allcoffee



if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
