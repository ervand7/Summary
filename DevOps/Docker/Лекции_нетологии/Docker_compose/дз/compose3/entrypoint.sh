#! /bin/bash

python manage.py makemigrations

python manage.py migrate

python manage.py collectstatic

python manage.py loaddata fixtures.json

exec gunicorn project_shop.wsgi:application -b 0.0.0.0:8000 --reload
