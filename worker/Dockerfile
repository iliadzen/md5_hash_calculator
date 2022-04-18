FROM python:3.7-slim

COPY worker/requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY worker/app/ .
COPY src/ src