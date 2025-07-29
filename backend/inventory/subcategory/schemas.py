from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class SubcategoryBase(BaseModel):
    name: str = Field(..., max_length=100, description="Name of the subcategory")
    description: Optional[str] = Field(None, max_length=255, description="Description of the subcategory")
    category_id: int = Field(..., description="ID of the parent category")

class SubcategoryCreate(SubcategoryBase):
    pass

class SubcategoryUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100, description="Name of the subcategory")
    description: Optional[str] = Field(None, max_length=255, description="Description of the subcategory")
    active: Optional[bool] = Field(None, description="Whether the subcategory is active")

class Subcategory(SubcategoryBase):
    id: int
    created_at: datetime
    updated_at: datetime
    active: bool

    class Config:
        from_attributes = True
