#!/bin/bash
# Test service i

#!/bin/bash
for i in 1 2 3 4
do
    cd service_$i
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    pip3 install pytest pytest-cov flask_testing requests_mock
    python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
    deactivate
    cd ..
done