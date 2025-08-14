from sqlalchemy import Column, Integer, String, DateTime, Boolean
from backend.db.base import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class ElectronicCards(Base):
    __tablename__ = "electronic_cards"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    code = Column(String(100))
    model = Column(String(100))
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    active = Column(Boolean, default=True)

    card_components = relationship("inventory.card_components.models.CardComponent", back_populates="electronic_card")
    display_electronic_cards = relationship(
        "inventory.models.DisplayElectronicCards", back_populates="electronic_card"
    )
    gabinete_electronic_cards = relationship(
        "inventory.models.GabineteElectronicCards", back_populates="electronic_card"
    )
    cartridge_electronic_cards = relationship(
        "inventory.models.CartridgeElectronicCards", back_populates="electronic_card"
    )
