#!/bin/bash

python3 manage.py migrate --no-output
python3 manage.py collectstatic --noinput

gunicorn studypadi.wsgi:application --bind 0.0.0.0:8000