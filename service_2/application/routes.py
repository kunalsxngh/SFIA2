from application import app
from flask import request, Response
import random
import string

def random_letters(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

@app.route("/", methods=["GET"])
def get_letters():
    letters = random_letters(5).upper()
    return Response(str(letters), mimetype='text/plain')