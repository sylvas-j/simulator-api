#!/bin/sh

python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn models_simulator.wsgi:application --bind 0.0.0.0:${APP_PORT}