#!/usr/bin/env sh

cd /code/
#npm install
#bower install --allow-root
#python manage.py migrate
#python manage.py collectstatic --noinput

python manage.py runserver 0.0.0.0:8080