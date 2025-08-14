from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PuertasBase(BaseModel):
    name: str
    description: Optional[str] = None
    active: Optional[bool] = True


class PuertasCreate(PuertasBase):
    pass


class PuertasUpdate(PuertasBase):
    pass


class PuertasOut(PuertasBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
