#!/bin/sh

echo 'Waiting for postgres...'

while ! nc -z $DB_HOSTNAME $DB_PORT; do
    sleep 0.1
done

echo 'PostgreSQL started'

echo 'Running migrations...'
./.venv/bin/python manage.py migrate

echo 'Collecting static files...'
./.venv/bin/python manage.py collectstatic --no-input

exec "$@"