from application import app, db
import requests
from flask import render_template
from sqlalchemy import desc
import json

class Numberplate(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    numberplate = db.Column(db.String(10), nullable=False)
    car_color = db.Column(db.String(10), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def index():

    letters_response = requests.get("http://numberplate-letters:5001") #container names
    numbers_response = requests.get("http://numberplate-numbers:5002")

    data = {"letters" : letters_response.text, "numbers" : numbers_response.text}
    numberplate_response = requests.post("http://numberplate-generator:5003", json = data)
    json_response = numberplate_response.json()

    
    new_number_plate = Numberplate(numberplate = json_response["numberplate"], car_color = json_response["color"])
    db.session.add(new_number_plate)
    db.session.commit()
    all_numberplates = Numberplate.query.order_by(desc("id")).limit(5).all()


    return render_template("index.html", numberplate = json_response["numberplate"], car_color = json_response["color"], all_numberplates = all_numberplates)

