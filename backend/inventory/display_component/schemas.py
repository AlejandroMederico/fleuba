from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DisplayComponentBase(BaseModel):
    display_id: int
    product_id: int
    quantity: Optional[int] = 1

class DisplayComponentCreate(DisplayComponentBase):
    pass

class DisplayComponentUpdate(DisplayComponentBase):
    pass

class DisplayComponentInDB(DisplayComponentBase):
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
