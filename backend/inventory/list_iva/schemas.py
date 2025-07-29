from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ListIvaBase(BaseModel):
    name: str = Field(..., max_length=100, description="Name of the IVA rate")
    rate: float = Field(..., ge=0, description="IVA rate percentage")
    description: Optional[str] = Field(None, max_length=255, description="Description of the IVA rate")

class ListIvaCreate(ListIvaBase):
    pass

class ListIvaUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100, description="Name of the IVA rate")
    rate: Optional[float] = Field(None, ge=0, description="IVA rate percentage")
    description: Optional[str] = Field(None, max_length=255, description="Description of the IVA rate")
    active: Optional[bool] = Field(None, description="Whether the IVA rate is active")

class ListIva(ListIvaBase):
    id: int
    created_at: datetime
    updated_at: datetime
    active: bool

    class Config:
        from_attributes = True
