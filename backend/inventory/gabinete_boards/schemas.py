from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class GabineteBoardsBase(BaseModel):
    gabinete_id: int
    board_id: int
    quantity: Optional[int] = 1

class GabineteBoardsCreate(GabineteBoardsBase):
    pass

class GabineteBoardsUpdate(GabineteBoardsBase):
    pass

class GabineteBoardsOut(GabineteBoardsBase):
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
