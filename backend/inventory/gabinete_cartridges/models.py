from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.db.base import Base
from datetime import datetime

class GabineteCartridges(Base):
    __tablename__ = "gabinete_cartridges"
    gabinete_id = Column(Integer, ForeignKey("gabinetes.id"), primary_key=True)
    cartridge_id = Column(Integer, ForeignKey("cartridges.id"), primary_key=True)
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    gabinete = relationship("inventory.models.Gabinetes", back_populates="gabinete_cartridges")
    cartridge = relationship("inventory.cartridges.models.Cartridges", back_populates="gabinete_cartridges")
