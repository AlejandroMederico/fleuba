from pydantic import BaseModel
from datetime import datetime


class CategoryBase(BaseModel):
    name: str
    description: str | None = None


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    created_at: datetime
    updated_at: datetime
    active: bool

    model_config = {"from_attributes": True}
