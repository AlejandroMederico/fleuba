from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.db.base import Base
from datetime import datetime

class BoardComponent(Base):
    __tablename__ = "board_component"
    board_id = Column(Integer, ForeignKey("boards.id"), primary_key=True)
    product_id = Column(Integer, ForeignKey("component.id"), primary_key=True)
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    board = relationship("Boards", back_populates="board_components")
    component = relationship("Component", back_populates="board_components")
