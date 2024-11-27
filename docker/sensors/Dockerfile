FROM python:3.13-slim

WORKDIR /code

COPY sensors/requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY sensors /code/
