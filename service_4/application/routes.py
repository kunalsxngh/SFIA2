from application import app
from flask import request, Response
from random import randrange
import json


@app.route("/", methods=["POST"])
def get_numberplate():
    data = request.json
    letters = data["letters"]
    years = int(data["numbers"])
    color = "yellow"
    if (years % 3 == 0):
        color = "red"
    if ('G' in letters):
        years += randrange(10)

    if (years < 10):
        year = "0" + str(years)
    else:
        year = str(years)
    
    numberplate = letters[:2] + year + letters[2:]
    car_information = {"numberplate" : numberplate, "color" : color}
    return Response(json.dumps(car_information))