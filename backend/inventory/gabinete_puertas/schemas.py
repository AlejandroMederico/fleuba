from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class GabinetePuertasBase(BaseModel):
    gabinete_id: int
    puerta_id: int
    quantity: Optional[int] = 1

class GabinetePuertasCreate(GabinetePuertasBase):
    pass

class GabinetePuertasUpdate(GabinetePuertasBase):
    pass

class GabinetePuertasOut(GabinetePuertasBase):
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
