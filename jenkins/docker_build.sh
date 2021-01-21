#!/bin/bash

/usr/local/bin/docker-compose build
docker login
/usr/local/bin/docker-compose push
