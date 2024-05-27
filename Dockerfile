FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code
RUN apt-get update \
    && apt-get -y install gettext \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

COPY requirements.txt .
RUN pip install -r requirements.txt 

COPY ./toothease .