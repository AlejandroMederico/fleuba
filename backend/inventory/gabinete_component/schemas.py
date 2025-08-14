from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class GabineteComponentBase(BaseModel):
    gabinete_id: int
    product_id: int
    quantity: Optional[int] = 1

class GabineteComponentCreate(GabineteComponentBase):
    pass

class GabineteComponentUpdate(GabineteComponentBase):
    pass

class GabineteComponentOut(GabineteComponentBase):
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
