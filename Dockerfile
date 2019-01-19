FROM python:3.7-alpine
MAINTAINER Petoandroide

ENV PYTHONUNBUFFERED 1

RUN pip install pipenv

COPY ./Pipfile /Pipfile
COPY ./Pipfile.lock /Pipfile.lock

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev

RUN pipenv install --system --deploy --ignore-pipfile

RUN apk del .tmp-build-deps

RUN adduser -D user
USER user
