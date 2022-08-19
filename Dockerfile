FROM python:3.8-slim-buster as base

WORKDIR /api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apt-get update \
    && apt-get -y install netcat gcc libpq-dev \
    && apt-get clean

RUN pip install pipenv

COPY Pipfile /api
COPY Pipfile.lock /api

RUN pipenv install --system --deploy --ignore-pipfile

COPY api /api