from sqlalchemy import Column, String, Float, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship
import uuid

Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    category = Column(String(255), nullable=False)
    username = Column(String(50), nullable=False)

    # Используйте множественное число для названия отношения, так как это коллекция
    spend = relationship("Spend", back_populates="category", cascade="all, delete-orphan")

class Spend(Base):
    __tablename__ = 'spend'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    username = Column(String(50), nullable=False)
    spend_date = Column(Date, nullable=False)
    currency = Column(String(50), nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String(255), nullable=False)
    category_id = Column(UUID(as_uuid=True), ForeignKey('category.id'), nullable=False)

    # Связь с таблицей category (опционально для удобства работы)
    category = relationship("Category", back_populates="spend")
