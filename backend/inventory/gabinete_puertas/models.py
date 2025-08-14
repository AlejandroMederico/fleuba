from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.db.base import Base
from datetime import datetime

class GabinetePuertas(Base):
    __tablename__ = "gabinete_puertas"
    gabinete_id = Column(Integer, ForeignKey("gabinetes.id"), primary_key=True)
    puerta_id = Column(Integer, ForeignKey("puertas.id"), primary_key=True)
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    gabinete = relationship("inventory.models.Gabinetes", back_populates="gabinete_puertas")
    puerta = relationship("inventory.puertas.models.Puertas", back_populates="gabinete_puertas")
