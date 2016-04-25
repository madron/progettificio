#!/usr/bin/env sh
rm -f db.sqlite3

./manage.py migrate --noinput --verbosity=1

./manage.py loaddata \
    sites \
    auth_admin \
    association_test
