from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class GabineteElectronicCardsBase(BaseModel):
    gabinete_id: int
    electronic_card_id: int
    quantity: Optional[int] = 1

class GabineteElectronicCardsCreate(GabineteElectronicCardsBase):
    pass

class GabineteElectronicCardsUpdate(GabineteElectronicCardsBase):
    pass

class GabineteElectronicCardsOut(GabineteElectronicCardsBase):
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
