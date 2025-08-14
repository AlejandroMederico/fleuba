from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.db.base import Base
from datetime import datetime

class PuertaComponent(Base):
    __tablename__ = "puerta_component"
    puerta_id = Column(Integer, ForeignKey("puertas.id"), primary_key=True)
    product_id = Column(Integer, ForeignKey("component.id"), primary_key=True)
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    puerta = relationship("inventory.puertas.models.Puertas", back_populates="puerta_components")
    component = relationship("inventory.models.Component", back_populates="puerta_components")
