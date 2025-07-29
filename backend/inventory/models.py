from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    ForeignKey,
    DateTime,
    Table,
)
from sqlalchemy.orm import relationship
from backend.db.base import Base
from datetime import datetime

# Import models from submodules to avoid circular imports
from .subcategory.models import Subcategory
from .list_iva.models import ListIva
from .list_vendors.models import ListVendors
from .product_vendor.models import ProductVendor


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

    category = relationship(
        "inventory.category.models.Category", back_populates="components"
    )
    subcategory = relationship(
        "inventory.subcategory.models.Subcategory", back_populates="components"
    )
    iva = relationship("inventory.list_iva.models.ListIva", back_populates="components")

    # Many-to-many relationship with ListVendors through ProductVendor
    vendors = relationship(
        "inventory.list_vendors.models.ListVendors",
        secondary="product_vendor",
        back_populates="products",
    )

    # Relationship with ProductVendor for additional attributes in the association table
    product_vendors = relationship(
        "inventory.product_vendor.models.ProductVendor", back_populates="product"
    )

    # Relationships with component types
    card_components = relationship("CardComponent", back_populates="component")
    cartridge_components = relationship(
        "CartridgeComponent", back_populates="component"
    )
    board_components = relationship("BoardComponent", back_populates="component")
    roof_components = relationship("RoofComponent", back_populates="component")
    display_components = relationship("DisplayComponent", back_populates="component")
    puerta_components = relationship("PuertaComponent", back_populates="component")
    gabinete_components = relationship("GabineteComponent", back_populates="component")

    # Relationship with ElectronicCards
    electronic_cards = relationship("ElectronicCards", back_populates="component")


class ElectronicCards(Base):
    __tablename__ = "electronic_cards"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    code = Column(String(100))
    model = Column(String(100))
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    active = Column(Boolean, default=True)

    card_components = relationship("CardComponent", back_populates="electronic_card")
    display_electronic_cards = relationship(
        "DisplayElectronicCards", back_populates="electronic_card"
    )
    gabinete_electronic_cards = relationship(
        "GabineteElectronicCards", back_populates="electronic_card"
    )


class CardComponent(Base):
    __tablename__ = "card_component"
    card_id = Column(Integer, ForeignKey("electronic_cards.id"), primary_key=True)
    product_id = Column(Integer, ForeignKey("component.id"), primary_key=True)
    assigned_at = Column(DateTime, default=datetime.utcnow)

    electronic_card = relationship("ElectronicCards", back_populates="card_components")
    component = relationship("Component", back_populates="card_components")


class Cartridges(Base):
    __tablename__ = "cartridges"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    active = Column(Boolean, default=True)

    cartridge_components = relationship(
        "CartridgeComponent", back_populates="cartridge"
    )
    cartridge_electronic_cards = relationship(
        "CartridgeElectronicCards", back_populates="cartridge"
    )


class CartridgeComponent(Base):
    __tablename__ = "cartridge_component"
    cartridge_id = Column(Integer, ForeignKey("cartridges.id"), primary_key=True)
    product_id = Column(Integer, ForeignKey("component.id"), primary_key=True)
    quantity = Column(Integer, default=1)

    cartridge = relationship("Cartridges", back_populates="cartridge_components")
    component = relationship("Component", back_populates="cartridge_components")


class CartridgeElectronicCards(Base):
    __tablename__ = "cartridge_electronic_cards"
    cartridge_id = Column(Integer, ForeignKey("cartridges.id"), primary_key=True)
    card_id = Column(Integer, ForeignKey("electronic_cards.id"), primary_key=True)
    quantity = Column(Integer, default=1)

    cartridge = relationship("Cartridges", back_populates="cartridge_electronic_cards")
    electronic_card = relationship(
        "ElectronicCards", back_populates="cartridge_electronic_cards"
    )


class Boards(Base):
    __tablename__ = "boards"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    active = Column(Boolean, default=True)

    board_components = relationship("BoardComponent", back_populates="board")


class BoardComponent(Base):
    __tablename__ = "board_component"
    board_id = Column(Integer, ForeignKey("boards.id"), primary_key=True)
    product_id = Column(Integer, ForeignKey("component.id"), primary_key=True)
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    board = relationship("Boards", back_populates="board_components")
    component = relationship("Component", back_populates="board_components")


class Roofs(Base):
    __tablename__ = "roofs"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    active = Column(Boolean, default=True)

    roof_components = relationship("RoofComponent", back_populates="roof")


class RoofComponent(Base):
    __tablename__ = "roof_component"
    roof_id = Column(Integer, ForeignKey("roofs.id"), primary_key=True)
    product_id = Column(Integer, ForeignKey("component.id"), primary_key=True)
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    roof = relationship("Roofs", back_populates="roof_components")
    component = relationship("Component", back_populates="roof_components")


class Display(Base):
    __tablename__ = "display"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    active = Column(Boolean, default=True)

    display_components = relationship("DisplayComponent", back_populates="display")
    display_electronic_cards = relationship(
        "DisplayElectronicCards", back_populates="display"
    )


class DisplayComponent(Base):
    __tablename__ = "display_component"
    display_id = Column(Integer, ForeignKey("display.id"), primary_key=True)
    product_id = Column(Integer, ForeignKey("component.id"), primary_key=True)
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    display = relationship("Display", back_populates="display_components")
    component = relationship("Component", back_populates="display_components")


class DisplayElectronicCards(Base):
    __tablename__ = "display_electronic_cards"
    display_id = Column(Integer, ForeignKey("display.id"), primary_key=True)
    card_id = Column(Integer, ForeignKey("electronic_cards.id"), primary_key=True)
    quantity = Column(Integer, default=1)

    display = relationship("Display", back_populates="display_electronic_cards")
    electronic_card = relationship(
        "ElectronicCards", back_populates="display_electronic_cards"
    )


class Puertas(Base):
    __tablename__ = "puertas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    active = Column(Boolean, default=True)

    puerta_components = relationship("PuertaComponent", back_populates="puerta")
    gabinete_puertas = relationship("GabinetePuertas", back_populates="puerta")


class PuertaComponent(Base):
    __tablename__ = "puerta_component"
    puerta_id = Column(Integer, ForeignKey("puertas.id"), primary_key=True)
    product_id = Column(Integer, ForeignKey("component.id"), primary_key=True)
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    puerta = relationship("Puertas", back_populates="puerta_components")
    component = relationship("Component", back_populates="puerta_components")


class Gabinetes(Base):
    __tablename__ = "gabinetes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    active = Column(Boolean, default=True)

    gabinete_puertas = relationship("GabinetePuertas", back_populates="gabinete")
    gabinete_components = relationship("GabineteComponent", back_populates="gabinete")
    gabinete_displays = relationship("GabineteDisplays", back_populates="gabinete")
    gabinete_roofs = relationship("GabineteRoofs", back_populates="gabinete")
    gabinete_boards = relationship("GabineteBoards", back_populates="gabinete")
    gabinete_cartridges = relationship("GabineteCartridges", back_populates="gabinete")
    gabinete_electronic_cards = relationship(
        "GabineteElectronicCards", back_populates="gabinete"
    )


class GabinetePuertas(Base):
    __tablename__ = "gabinete_puertas"
    gabinete_id = Column(Integer, ForeignKey("gabinetes.id"), primary_key=True)
    puerta_id = Column(Integer, ForeignKey("puertas.id"), primary_key=True)
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    gabinete = relationship("Gabinetes", back_populates="gabinete_puertas")
    puerta = relationship("Puertas", back_populates="gabinete_puertas")


class GabineteComponent(Base):
    __tablename__ = "gabinete_component"
    gabinete_id = Column(Integer, ForeignKey("gabinetes.id"), primary_key=True)
    product_id = Column(Integer, ForeignKey("component.id"), primary_key=True)
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    gabinete = relationship("Gabinetes", back_populates="gabinete_components")
    component = relationship("Component", back_populates="gabinete_components")


class GabineteDisplays(Base):
    __tablename__ = "gabinete_displays"
    gabinete_id = Column(Integer, ForeignKey("gabinetes.id"), primary_key=True)
    display_id = Column(Integer, ForeignKey("display.id"), primary_key=True)
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    gabinete = relationship("Gabinetes", back_populates="gabinete_displays")
    display = relationship("Display", back_populates="gabinete_displays")


class GabineteRoofs(Base):
    __tablename__ = "gabinete_roofs"
    gabinete_id = Column(Integer, ForeignKey("gabinetes.id"), primary_key=True)
    roof_id = Column(Integer, ForeignKey("roofs.id"), primary_key=True)
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    gabinete = relationship("Gabinetes", back_populates="gabinete_roofs")
    roof = relationship("Roofs", back_populates="gabinete_roofs")


class GabineteBoards(Base):
    __tablename__ = "gabinete_boards"
    gabinete_id = Column(Integer, ForeignKey("gabinetes.id"), primary_key=True)
    board_id = Column(Integer, ForeignKey("boards.id"), primary_key=True)
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    gabinete = relationship("Gabinetes", back_populates="gabinete_boards")
    board = relationship("Boards", back_populates="gabinete_boards")


class GabineteCartridges(Base):
    __tablename__ = "gabinete_cartridges"
    gabinete_id = Column(Integer, ForeignKey("gabinetes.id"), primary_key=True)
    cartridge_id = Column(Integer, ForeignKey("cartridges.id"), primary_key=True)
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    gabinete = relationship("Gabinetes", back_populates="gabinete_cartridges")
    cartridge = relationship("Cartridges", back_populates="gabinete_cartridges")


class GabineteElectronicCards(Base):
    __tablename__ = "gabinete_electronic_cards"
    gabinete_id = Column(Integer, ForeignKey("gabinetes.id"), primary_key=True)
    electronic_card_id = Column(
        Integer, ForeignKey("electronic_cards.id"), primary_key=True
    )
    quantity = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    gabinete = relationship("Gabinetes", back_populates="gabinete_electronic_cards")
    electronic_card = relationship(
        "ElectronicCards", back_populates="gabinete_electronic_cards"
    )
