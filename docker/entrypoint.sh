#!/bin/bash
set -e

if [ "$1" = 'uwsgi' ]; then
    chown -R uwsgi:uwsgi /run/uwsgi
    chown -R uwsgi:uwsgi /media
    gosu uwsgi /src/manage.py migrate --noinput
    exec gosu uwsgi uwsgi "${@:2}"
elif [ "$1" = 'nginx' ]; then
    exec nginx "-g daemon off;"
else
    exec "$@"
fi
