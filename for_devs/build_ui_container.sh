#! /bin/bash

cd ../web/web-app/

set -e

sudo docker build -t $1 .

sudo docker push $1
