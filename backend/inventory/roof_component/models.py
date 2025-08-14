from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.db.base import Base
from datetime import datetime

class RoofComponent(Base):
    __tablename__ = "roof_component"
    roof_id = Column(Integer, ForeignKey("roofs.id"), primary_key=True)
    product_id = Column(Integer, ForeignKey("component.id"), primary_key=True)
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    roof = relationship("Roofs", back_populates="roof_components")
    component = relationship("Component", back_populates="roof_components")
