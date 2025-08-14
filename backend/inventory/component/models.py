from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.db.base import Base
from datetime import datetime

class Component(Base):
    __tablename__ = "component"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    code = Column(String(50))
    description = Column(String(500))
    cost = Column(Float)
    category_id = Column(Integer, ForeignKey("categories.id"))
    subcategory_id = Column(Integer, ForeignKey("subcategories.id"))
    iva_id = Column(Integer, ForeignKey("list_iva.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    active = Column(Boolean, default=True)

    category = relationship("inventory.category.models.Category", back_populates="components")
    subcategory = relationship("inventory.subcategory.models.Subcategory", back_populates="components")
    iva = relationship("inventory.list_iva.models.ListIva", back_populates="components")

    vendors = relationship("inventory.list_vendors.models.ListVendors", secondary="product_vendor", back_populates="products")
    product_vendors = relationship("inventory.product_vendor.models.ProductVendor", back_populates="product")

    card_components = relationship("inventory.card_components.models.CardComponent", back_populates="component")
    cartridge_components = relationship("inventory.cartridge_component.models.CartridgeComponent", back_populates="component")
    board_components = relationship("inventory.board_component.models.BoardComponent", back_populates="component")
    roof_components = relationship("inventory.roof_component.models.RoofComponent", back_populates="component")
    display_components = relationship("inventory.display_component.models.DisplayComponent", back_populates="component")
    puerta_components = relationship("inventory.puerta_component.models.PuertaComponent", back_populates="component")
    gabinete_components = relationship("inventory.gabinete_component.models.GabineteComponent", back_populates="component")

    electronic_cards = relationship("inventory.electronic_cards.models.ElectronicCards", back_populates="component")
