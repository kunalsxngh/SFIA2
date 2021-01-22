#!/bin/bash
# Test service i

python3 -m venv venv
source venv/bin/activate
pip3 install pytest pytest-cov flask_testing requests_mock flask_sqlalchemy
pip3 install -r service_1/requirements.txt

for i in 1 2 3 4
do
    cd service_$i
    python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
    cd ..
done
deactivate