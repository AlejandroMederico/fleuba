from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CardComponentBase(BaseModel):
    assigned_at: Optional[datetime] = None


class CardComponentCreate(CardComponentBase):
    card_id: int
    product_id: int


class CardComponentUpdate(CardComponentBase):
    pass


class CardComponent(CardComponentBase):
    card_id: int
    product_id: int
    assigned_at: datetime

    class Config:
        orm_mode = True
