FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY api/requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY api/app /app
COPY src /app/src