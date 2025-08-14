from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class GabineteRoofsBase(BaseModel):
    gabinete_id: int
    roof_id: int
    quantity: Optional[int] = 1

class GabineteRoofsCreate(GabineteRoofsBase):
    pass

class GabineteRoofsUpdate(GabineteRoofsBase):
    pass

class GabineteRoofsOut(GabineteRoofsBase):
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
