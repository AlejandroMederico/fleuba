from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class DisplayBase(BaseModel):
    name: str
    description: Optional[str] = None
    active: Optional[bool] = True


class DisplayCreate(DisplayBase):
    pass


class DisplayUpdate(DisplayBase):
    pass


class DisplayInDB(DisplayBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
