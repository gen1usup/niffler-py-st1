from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship
import uuid

Base = declarative_base()

class UserAuth(Base):
    __tablename__ = 'user' # указываем схему auth, если она используется

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)
    enabled = Column(Boolean, nullable=False)
    account_non_expired = Column(Boolean, nullable=False)
    account_non_locked = Column(Boolean, nullable=False)
    credentials_non_expired = Column(Boolean, nullable=False)

    authorities = relationship("Authority", back_populates="user")

class Authority(Base):
    __tablename__ = 'authority'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'), nullable=False)
    authority = Column(String(50), nullable=False)

    user = relationship("UserAuth", back_populates="authorities")
