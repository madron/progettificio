#!/bin/bash

set -e

docker build -t madron/progettificio .
docker tag madron/progettificio madron/progettificio:`hg identify --num -r .`
echo
echo "Succesfully built image madron/progettificio:`hg identify --num -r .`"
echo "To publish execute:"
echo "docker push madron/progettificio:`hg identify --num -r .`"
