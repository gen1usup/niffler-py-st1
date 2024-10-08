from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID, BYTEA
from sqlalchemy.orm import declarative_base
import uuid

Base = declarative_base()

class UserUserdata(Base):
    __tablename__ = 'user'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    username = Column(String(50), nullable=False)
    currency = Column(String(3), nullable=False)
    firstname = Column(String(255), nullable=True)
    surname = Column(String(255), nullable=True)
    photo = Column(BYTEA, nullable=True)
    photo_small = Column(BYTEA, nullable=True)


class User:
    pass