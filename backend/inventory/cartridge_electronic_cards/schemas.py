from pydantic import BaseModel
from typing import Optional

class CartridgeElectronicCardsBase(BaseModel):
    quantity: Optional[int] = 1

class CartridgeElectronicCardsCreate(CartridgeElectronicCardsBase):
    cartridge_id: int
    card_id: int

class CartridgeElectronicCardsUpdate(CartridgeElectronicCardsBase):
    pass

class CartridgeElectronicCards(CartridgeElectronicCardsBase):
    cartridge_id: int
    card_id: int
    quantity: int

    class Config:
        orm_mode = True
