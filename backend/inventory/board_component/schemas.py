from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BoardComponentBase(BaseModel):
    board_id: int
    product_id: int
    quantity: Optional[int] = 1

class BoardComponentCreate(BoardComponentBase):
    pass

class BoardComponentUpdate(BoardComponentBase):
    pass

class BoardComponentInDB(BoardComponentBase):
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
