from application import app
from flask import request, Response
import random


@app.route("/", methods=["GET"])
def get_numbers():
    year = random.randint(1990, 2021)
    return Response(str(year)[-2:], mimetype='text/plain')