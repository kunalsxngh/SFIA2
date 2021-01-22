from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
import requests_mock

from application import app, db
from application.routes import Numberplate

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///")
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Numberplate(numberplate="TEST", car_color="test"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestResponse(TestBase):
   
    def test_numberplate(self):
        with requests_mock.mock() as m:
            m.get('http://numberplate-stack_letters:5001', text='ABCDE')
            m.get('http://numberplate-stack_numberplate-numbers:5002', text='21')
            data = {"numberplate" : 'AB21CDE', "color" : 'yellow'}
            m.post('http://numberplate-stack_numberplate-generator:5003', json=data)
            response = self.client.get(url_for('index'))
            self.assertIn(b'AB21CDE', response.data)
            self.assertIn(b'TEST had the car color test', response.data)