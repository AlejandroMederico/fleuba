from pydantic import BaseModel
from typing import Optional

class CartridgeComponentBase(BaseModel):
    quantity: Optional[int] = 1

class CartridgeComponentCreate(CartridgeComponentBase):
    cartridge_id: int
    product_id: int

class CartridgeComponentUpdate(CartridgeComponentBase):
    pass

class CartridgeComponent(CartridgeComponentBase):
    cartridge_id: int
    product_id: int
    quantity: int

    class Config:
        orm_mode = True
