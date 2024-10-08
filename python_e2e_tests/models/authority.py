# from sqlalchemy import Column, String, ForeignKey
# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy.orm import declarative_base, relationship
# import uuid
#
# Base = declarative_base()
#
# class Authority(Base):
#     __tablename__ = 'authority'
#
#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
#     user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'), nullable=False)
#     authority = Column(String(50), nullable=False)
#
#     user = relationship("UserAuth", back_populates="authorities")
