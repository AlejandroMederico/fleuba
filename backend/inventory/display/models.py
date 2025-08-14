from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from backend.db.base import Base
from datetime import datetime


class Display(Base):
    __tablename__ = "display"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    active = Column(Boolean, default=True)

    display_components = relationship(
        "inventory.display.models.DisplayComponent", back_populates="display"
    )
    display_electronic_cards = relationship(
        "inventory.display.models.DisplayElectronicCards", back_populates="display"
    )
