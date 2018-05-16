FROM python:3.6-alpine3.7

COPY . /code/

RUN apk update && \
    apk upgrade && \
    apk add --upgrade apk-tools && \
    apk add nodejs git && \
    apk add build-base python3-dev jpeg-dev zlib-dev && \
    npm install -g bower gulp && \
    cd /code/ && npm install && bower install --allow-root && \
    pip install --upgrade pip setuptools && \
    pip install --upgrade -r /code/requirements.txt && \
    python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py collectstatic --noinput && \
    npm remove bower gulp && \
    apk del apk-tools python-dev git nodejs build-base

