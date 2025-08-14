from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class GabineteDisplaysBase(BaseModel):
    gabinete_id: int
    display_id: int
    quantity: Optional[int] = 1

class GabineteDisplaysCreate(GabineteDisplaysBase):
    pass

class GabineteDisplaysUpdate(GabineteDisplaysBase):
    pass

class GabineteDisplaysOut(GabineteDisplaysBase):
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
