from celery import Celery
from config import BROKER_URL, RESULT_BACKEND_URL

celery_app = Celery(
    'worker',
    broker=BROKER_URL,
    backend=RESULT_BACKEND_URL
)
