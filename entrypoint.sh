#!/usr/bin/env sh

#cd /code/
#npm install
#bower install --allow-root
#python manage.py migrate
#python manage.py collectstatic --noinput

cd /code/
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
npm install . 
rm -rf `pwd`/static/node_modules
cp -r `pwd`/node_modules `pwd`/static/
ls -al `pwd`/static/
ls -al `pwd`
python manage.py runserver 0.0.0.0:8080
