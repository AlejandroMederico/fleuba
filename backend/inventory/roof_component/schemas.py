from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RoofComponentBase(BaseModel):
    roof_id: int
    product_id: int
    quantity: Optional[int] = 1

class RoofComponentCreate(RoofComponentBase):
    pass

class RoofComponentUpdate(RoofComponentBase):
    pass

class RoofComponentInDB(RoofComponentBase):
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
