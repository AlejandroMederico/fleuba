from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.db.base import Base
from datetime import datetime


class Puertas(Base):
    __tablename__ = "puertas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    active = Column(Boolean, default=True)

    puerta_components = relationship(
        "inventory.puertas.models.PuertaComponent", back_populates="puerta"
    )
    gabinete_puertas = relationship(
        "inventory.puertas.models.GabinetePuertas", back_populates="puerta"
    )
