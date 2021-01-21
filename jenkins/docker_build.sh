#!/bin/bash

docker login -u= "$docker_credentials.USR" -p="$docker_credentials.PSW"
/usr/local/bin/docker-compose build
/usr/local/bin/docker-compose push
