FROM python:3.7-alpine
MAINTAINER Petoandroide

ENV PYTHONUNBUFFERED 1

RUN pip install pipenv

COPY ./Pipfile /Pipfile
COPY ./Pipfile.lock /Pipfile.lock

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN pipenv install --system --deploy --ignore-pipfile
RUN adduser -D user
USER user
