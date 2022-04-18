from os import environ

BROKER_URL = 'amqp://guest:guest@rabbitmq:5672//'
RESULT_BACKEND_URL = 'redis://redis:6379/0'

PG_USER = environ.get('POSTGRES_USER')
PG_PASS = environ.get('POSTGRES_PASSWORD')
DB_NAME = environ.get('POSTGRES_DB')

DB_URL = f"postgresql://{PG_USER}:{PG_PASS}@db/{DB_NAME}"
