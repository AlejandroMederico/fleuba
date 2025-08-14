from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RoofsBase(BaseModel):
    name: str
    description: Optional[str] = None
    active: Optional[bool] = True

class RoofsCreate(RoofsBase):
    pass

class RoofsUpdate(RoofsBase):
    pass

class RoofsInDB(RoofsBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
