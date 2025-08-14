from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.db.base import Base
from datetime import datetime

class GabineteRoofs(Base):
    __tablename__ = "gabinete_roofs"
    gabinete_id = Column(Integer, ForeignKey("gabinetes.id"), primary_key=True)
    roof_id = Column(Integer, ForeignKey("roofs.id"), primary_key=True)
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    gabinete = relationship("inventory.models.Gabinetes", back_populates="gabinete_roofs")
    roof = relationship("inventory.roofs.models.Roofs", back_populates="gabinete_roofs")
