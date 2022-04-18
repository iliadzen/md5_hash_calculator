from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session
import shutil
import uuid
from celery import Celery

from config import BROKER_URL, RESULT_BACKEND_URL
from database import get_db
from src.db.repository import get_hash

celery = Celery(
    'worker',
    broker=BROKER_URL,
    backend=RESULT_BACKEND_URL
)

router = APIRouter()


@router.post("/")
def upload_file(file: UploadFile = File(...)):
    id = uuid.uuid4()

    try:
        with open(f'data/{id}', "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    finally:
        file.file.close()

    celery.send_task('tasks.hash_file', kwargs={'id': id})

    return {"id": id}


@router.get("/{file_id}")
def get_file_hash(id: str, db: Session = Depends(get_db)):
    return get_hash(db, id)
