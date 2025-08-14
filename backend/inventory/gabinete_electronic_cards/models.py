from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.db.base import Base
from datetime import datetime

class GabineteElectronicCards(Base):
    __tablename__ = "gabinete_electronic_cards"
    gabinete_id = Column(Integer, ForeignKey("gabinetes.id"), primary_key=True)
    electronic_card_id = Column(Integer, ForeignKey("electronic_cards.id"), primary_key=True)
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    gabinete = relationship("inventory.models.Gabinetes", back_populates="gabinete_electronic_cards")
    electronic_card = relationship("inventory.electronic_cards.models.ElectronicCards", back_populates="gabinete_electronic_cards")
