from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PuertaComponentBase(BaseModel):
    puerta_id: int
    product_id: int
    quantity: Optional[int] = 1

class PuertaComponentCreate(PuertaComponentBase):
    pass

class PuertaComponentUpdate(PuertaComponentBase):
    pass

class PuertaComponentOut(PuertaComponentBase):
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
