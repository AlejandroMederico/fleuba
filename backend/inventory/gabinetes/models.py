from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from backend.db.base import Base
from datetime import datetime

class Gabinetes(Base):
    __tablename__ = "gabinetes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    active = Column(Boolean, default=True)

    gabinete_puertas = relationship("inventory.puertas.models.GabinetePuertas", back_populates="gabinete")
    gabinete_components = relationship("inventory.gabinete_component.models.GabineteComponent", back_populates="gabinete")
    gabinete_displays = relationship("inventory.gabinete_displays.models.GabineteDisplays", back_populates="gabinete")
    gabinete_roofs = relationship("inventory.gabinete_roofs.models.GabineteRoofs", back_populates="gabinete")
    gabinete_boards = relationship("inventory.gabinete_boards.models.GabineteBoards", back_populates="gabinete")
    gabinete_cartridges = relationship("inventory.gabinete_cartridges.models.GabineteCartridges", back_populates="gabinete")
    gabinete_electronic_cards = relationship("inventory.gabinete_electronic_cards.models.GabineteElectronicCards", back_populates="gabinete")
