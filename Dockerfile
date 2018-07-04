FROM python:3.6-alpine3.7

COPY . /code/

RUN apk update && \
    apk upgrade && \
    apk add --upgrade apk-tools && \
    apk add nodejs git && \
    apk add build-base python3-dev jpeg-dev zlib-dev && \
    pip install --upgrade pip setuptools && \
    pip install --upgrade -r /code/requirements.txt && \
    cd /code/ && \
    apk del apk-tools python-dev git build-base

