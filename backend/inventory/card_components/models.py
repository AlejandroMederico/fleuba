from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.db.base import Base
from datetime import datetime


class CardComponent(Base):
    __tablename__ = "card_component"
    card_id = Column(Integer, ForeignKey("electronic_cards.id"), primary_key=True)
    product_id = Column(Integer, ForeignKey("component.id"), primary_key=True)
    assigned_at = Column(DateTime, default=datetime.utcnow)

    # Relaciones
    electronic_card = relationship("inventory.electronic_cards.models.ElectronicCards", back_populates="card_components")
    component = relationship("inventory.models.Component", back_populates="card_components")
