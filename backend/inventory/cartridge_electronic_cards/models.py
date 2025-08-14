from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from backend.db.base import Base

class CartridgeElectronicCards(Base):
    __tablename__ = "cartridge_electronic_cards"
    cartridge_id = Column(Integer, ForeignKey("cartridges.id"), primary_key=True)
    card_id = Column(Integer, ForeignKey("electronic_cards.id"), primary_key=True)
    quantity = Column(Integer, default=1)

    cartridge = relationship("inventory.cartridges.models.Cartridges", back_populates="cartridge_electronic_cards")
    electronic_card = relationship("inventory.electronic_cards.models.ElectronicCards", back_populates="cartridge_electronic_cards")
