from time import sleep
from celery_app import celery_app
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from src.db.repository import create_hash
from hashing import generate_hash
from config import DB_URL

engine = create_engine(DB_URL)
Session = sessionmaker(engine)


@celery_app.task()
def test_celery(time: int):
    sleep(time)


@celery_app.task()
def hash_file(id: str):
    with Session() as db:
        create_hash(db, id, generate_hash('data/' + id))
