from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class GabinetesBase(BaseModel):
    name: str
    description: Optional[str] = None
    active: Optional[bool] = True

class GabinetesCreate(GabinetesBase):
    pass

class GabinetesUpdate(GabinetesBase):
    pass

class GabinetesOut(GabinetesBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
