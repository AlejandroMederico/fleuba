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

# Centraliza los imports de todos los modelos principales para facilitar migraciones y relaciones.
from .component.models import Component
from .category.models import Category
from .subcategory.models import Subcategory
from .list_iva.models import ListIva
from .list_vendors.models import ListVendors
from .product_vendor.models import ProductVendor
from .electronic_cards.models import ElectronicCards
from .cartridges.models import Cartridges
from .card_components.models import CardComponent
from .cartridge_component.models import CartridgeComponent
from .cartridge_electronic_cards.models import CartridgeElectronicCards
from .boards.models import Boards
from .board_component.models import BoardComponent
from .roofs.models import Roofs
from .roof_component.models import RoofComponent
from .display.models import Display
from .display_component.models import DisplayComponent
from .puertas.models import Puertas
from .puerta_component.models import PuertaComponent
from .gabinete_puertas.models import GabinetePuertas
from .gabinete_component.models import GabineteComponent
from .gabinete_displays.models import GabineteDisplays
from .gabinete_roofs.models import GabineteRoofs
from .gabinete_boards.models import GabineteBoards
from .gabinete_cartridges.models import GabineteCartridges
from .gabinetes.models import Gabinetes
