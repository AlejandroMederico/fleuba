from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BoardsBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    active: bool = True

class BoardsCreate(BoardsBase):
    name: str

class BoardsUpdate(BoardsBase):
    pass

class Boards(BoardsBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
