from sqlalchemy.orm import Session

from .models import Hash


def get_hash(db: Session, id: str):
    return db.query(Hash).filter(Hash.id == id).first()


def create_hash(db: Session, id: str, hash: str):
    db_hash = Hash(id=id, hash=hash)
    db.add(db_hash)
    db.commit()
    db.refresh(db_hash)
    return db_hash
