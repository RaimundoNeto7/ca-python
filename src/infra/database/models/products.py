from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String

from src.infra.database.config import Base


class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, index=True)
    description = Column(String)
    brand = Column(String(50), nullable=False, index=True)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    class Config:
        orm_mode = True
