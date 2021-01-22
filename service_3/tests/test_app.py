from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app



class TestResponse(TestBase):
   
    def test_get_numbers(self):
        with patch('random.randint') as random:
            random.return_value = "1990"
            response = self.client.get(url_for('get_numbers'))
            self.assertEqual(b'90', response.data)

            random.return_value = "2015"
            response = self.client.get(url_for('get_numbers'))
            self.assertEqual(b'15', response.data)

            random.return_value = "2001"
            response = self.client.get(url_for('get_numbers'))
            self.assertEqual(b'01', response.data)
