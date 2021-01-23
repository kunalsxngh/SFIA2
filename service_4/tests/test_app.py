from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import json
import requests_mock
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app



class TestResponse(TestBase):
   
    def test_get_numberplate(self):
        data = {"letters" : 'ABCDE', "numbers" : '15'}
        response = self.client.post(url_for('get_numberplate'), json=data)
        json_response = response.data
        test_json = b'{"numberplate": "AB15CDE", "color": "blue"}'
        assert json_response == test_json

        with patch('random.randrange') as random:
            random.return_value = "5"
            data = {"letters" : 'ABCDG', "numbers" : '9'}
            response = self.client.post(url_for('get_numberplate'), json=data)
            test_json = b'{"numberplate": "AB14CDG", "color": "blue"}'
        
        data = {"letters" : 'ABCDE', "numbers" : '4'}
        response = self.client.post(url_for('get_numberplate'), json=data)
        json_response = response.data
        test_json = b'{"numberplate": "AB04CDE", "color": "yellow"}'
        assert json_response == test_json
