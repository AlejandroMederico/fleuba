from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ComponentBase(BaseModel):
    name: str
    code: Optional[str] = None
    description: Optional[str] = None
    cost: Optional[float] = None
    category_id: Optional[int] = None
    subcategory_id: Optional[int] = None
    iva_id: Optional[int] = None
    active: Optional[bool] = True

class ComponentCreate(ComponentBase):
    pass

class ComponentUpdate(ComponentBase):
    pass

class ComponentOut(ComponentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
