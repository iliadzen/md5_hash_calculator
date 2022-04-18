from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Hash(Base):
    __tablename__ = "hashes"

    id = Column(UUID(as_uuid=True), primary_key=True)
    hash = Column(String, nullable=False)
