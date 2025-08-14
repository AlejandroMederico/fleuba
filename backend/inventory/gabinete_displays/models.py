from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.db.base import Base
from datetime import datetime

class GabineteDisplays(Base):
    __tablename__ = "gabinete_displays"
    gabinete_id = Column(Integer, ForeignKey("gabinetes.id"), primary_key=True)
    display_id = Column(Integer, ForeignKey("display.id"), primary_key=True)
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    gabinete = relationship("inventory.models.Gabinetes", back_populates="gabinete_displays")
    display = relationship("inventory.display.models.Display", back_populates="gabinete_displays")
