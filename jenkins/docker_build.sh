#!/bin/bash

docker login -u $docker_credentials_USR -p $docker_credentials_PSW
/usr/local/bin/docker-compose build
/usr/local/bin/docker-compose push
