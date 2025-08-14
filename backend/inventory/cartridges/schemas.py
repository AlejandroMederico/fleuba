from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CartridgesBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    active: bool = True

class CartridgesCreate(CartridgesBase):
    name: str

class CartridgesUpdate(CartridgesBase):
    pass

class Cartridges(CartridgesBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
