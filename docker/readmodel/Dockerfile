FROM python:3.13-slim

WORKDIR /code

COPY readmodel/requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY readmodel /code/
