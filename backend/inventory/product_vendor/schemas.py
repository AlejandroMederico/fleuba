from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional

class ProductVendorBase(BaseModel):
    """Base schema for ProductVendor with common fields."""
    cost: float = Field(..., gt=0, description="Cost of the product from this vendor")
    product_id: int = Field(..., description="ID of the product (component)")
    vendor_id: int = Field(..., description="ID of the vendor")

class ProductVendorCreate(ProductVendorBase):
    """Schema for creating a new product-vendor relationship."""
    pass

class ProductVendorUpdate(BaseModel):
    """Schema for updating a product-vendor relationship."""
    cost: Optional[float] = Field(None, gt=0, description="Updated cost of the product from this vendor")
    
    @validator('*', pre=True)
    def disallow_none(cls, v, field):
        if field.name == 'cost' and v is None:
            raise ValueError("Cost cannot be None when updating")
        return v

class ProductVendorInDBBase(ProductVendorBase):
    """Base schema for ProductVendor in the database."""
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class ProductVendor(ProductVendorInDBBase):
    """Schema for returning a product-vendor relationship."""
    pass

class ProductVendorWithDetails(ProductVendorInDBBase):
    """Schema for returning a product-vendor relationship with related data."""
    product_name: Optional[str] = Field(None, description="Name of the product")
    vendor_name: Optional[str] = Field(None, description="Name of the vendor")
