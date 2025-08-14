from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ElectronicCardBase(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    model: Optional[str] = None
    description: Optional[str] = None
    active: bool = True

class ElectronicCardCreate(ElectronicCardBase):
    name: str
    code: str
    model: str

class ElectronicCardUpdate(ElectronicCardBase):
    pass

class ElectronicCard(ElectronicCardBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
