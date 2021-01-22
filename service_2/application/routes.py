from application import app
from flask import request, Response
import random
import string

def random_letters():
       return ''.join(random.choice(string.ascii_letters) for x in range(5))

@app.route("/", methods=["GET"])
def get_letters():
    letters = random_letters().upper()
    return Response(str(letters), mimetype='text/plain')