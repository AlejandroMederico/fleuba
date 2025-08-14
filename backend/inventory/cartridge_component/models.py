from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from backend.db.base import Base

class CartridgeComponent(Base):
    __tablename__ = "cartridge_component"
    cartridge_id = Column(Integer, ForeignKey("cartridges.id"), primary_key=True)
    product_id = Column(Integer, ForeignKey("component.id"), primary_key=True)
    quantity = Column(Integer, default=1)

    cartridge = relationship("inventory.cartridges.models.Cartridges", back_populates="cartridge_components")
    component = relationship("inventory.models.Component", back_populates="cartridge_components")
