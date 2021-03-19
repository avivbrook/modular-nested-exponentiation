FROM python:3.9.2-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get clean

RUN pip install --upgrade pip
RUN pip install mod-nest-exp