from .component.models import Component
from .category.models import Category
from .subcategory.models import Subcategory
from .list_iva.models import ListIva
from .list_vendors.models import ListVendors
from .product_vendor.models import ProductVendor
from .electronic_cards.models import (
    ElectronicCards,
)  # Agregado para mantener la compatibilidad con la estructura anterior
from .card_components.models import (
    CardComponent,
)  # Importación agregada para la nueva ubicación
from .cartridges.models import Cartridges  # Importación agregada
from .cartridge_component.models import CartridgeComponent  # Importación agregada
from .cartridge_electronic_cards.models import (
    CartridgeElectronicCards,
)  # Importación agregada
from .boards.models import Boards  # Importación agregada
from .board_component.models import BoardComponent  # New import added
from .roofs.models import Roofs  # Only Roofs imported
from .roof_component.models import RoofComponent  # New import added
from .display.models import Display  # Solo Display importado
from .display_component.models import DisplayComponent
from .puertas.models import Puertas  # Importación agregada
from .puerta_component.models import PuertaComponent  # Importación agregada
from .gabinete_puertas.models import GabinetePuertas  # Importación agregada
from .gabinete_component.models import GabineteComponent  # New import added
from .gabinete_displays.models import GabineteDisplays  # New import added
from .gabinete_roofs.models import GabineteRoofs  # New import added
from .gabinete_boards.models import GabineteBoards  # New import added
from .gabinete_cartridges.models import GabineteCartridges  # New import added
from .gabinetes.models import Gabinetes  # New import added

# Re-export for easier imports
__all__ = [
    "Component",
    "Category",
    "Subcategory",
    "ListIva",
    "ListVendors",
    "ProductVendor",
    "ElectronicCards",
    "CardComponent",
    "Cartridges",
    "CartridgeComponent",
    "CartridgeElectronicCards",
    "Boards",
    "BoardComponent",
    "Roofs",
    "RoofComponent",
    "Display",
    "DisplayComponent",
    "Puertas",
    "PuertaComponent",
    "GabinetePuertas",
    "GabineteComponent",
    "GabineteDisplays",
    "GabineteRoofs",
    "GabineteBoards",
    "GabineteCartridges",
    "Gabinetes",
]
