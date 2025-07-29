from sqlalchemy import Column, Integer, String, DateTime, Boolean
from backend.db.base import Base  # Ajusta el import según tu estructura real
from datetime import datetime
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    active = Column(Boolean, default=True)

    subcategories = relationship("inventory.subcategory.models.Subcategory", back_populates="category")
    components = relationship("inventory.models.Component", back_populates="category")
