from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from backend.db.base import Base
from datetime import datetime

class Cartridges(Base):
    __tablename__ = "cartridges"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    active = Column(Boolean, default=True)

    cartridge_components = relationship("inventory.models.CartridgeComponent", back_populates="cartridge")
    cartridge_electronic_cards = relationship("inventory.models.CartridgeElectronicCards", back_populates="cartridge")
