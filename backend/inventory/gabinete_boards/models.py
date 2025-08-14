from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.db.base import Base
from datetime import datetime

class GabineteBoards(Base):
    __tablename__ = "gabinete_boards"
    gabinete_id = Column(Integer, ForeignKey("gabinetes.id"), primary_key=True)
    board_id = Column(Integer, ForeignKey("boards.id"), primary_key=True)
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    gabinete = relationship("inventory.models.Gabinetes", back_populates="gabinete_boards")
    board = relationship("inventory.boards.models.Boards", back_populates="gabinete_boards")
