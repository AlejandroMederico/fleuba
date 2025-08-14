from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.db.base import Base
from datetime import datetime

class DisplayComponent(Base):
    __tablename__ = "display_component"
    display_id = Column(Integer, ForeignKey("display.id"), primary_key=True)
    product_id = Column(Integer, ForeignKey("component.id"), primary_key=True)
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    display = relationship("inventory.display.models.Display", back_populates="display_components")
    component = relationship("inventory.models.Component", back_populates="display_components")
