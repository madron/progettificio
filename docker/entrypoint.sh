#!/bin/bash
set -e

chown -R uwsgi:uwsgi /media

if [ "$1" = 'uwsgi' ]; then
    chown -R uwsgi:uwsgi /run/uwsgi
    gosu uwsgi /src/manage.py migrate --noinput
    exec gosu uwsgi uwsgi "${@:2}"
elif [ "$1" = 'nginx' ]; then
    exec nginx "-g daemon off;"
else
    exec "$@"
fi
