from sqlalchemy import Column, String, Float, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship
import uuid

from python_e2e_tests.models.category import Category

Base = declarative_base()

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

# Добавляем обратную связь в модель Category
Category.spend = relationship("Spend", order_by=Spend.id, back_populates="category")
