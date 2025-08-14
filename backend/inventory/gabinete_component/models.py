from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.db.base import Base
from datetime import datetime

class GabineteComponent(Base):
    __tablename__ = "gabinete_component"
    gabinete_id = Column(Integer, ForeignKey("gabinetes.id"), primary_key=True)
    product_id = Column(Integer, ForeignKey("component.id"), primary_key=True)
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    gabinete = relationship("inventory.models.Gabinetes", back_populates="gabinete_components")
    component = relationship("inventory.models.Component", back_populates="gabinete_components")
