from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import Optional, List

class VendorBase(BaseModel):
    name: str = Field(..., max_length=100, description="Vendor's name")
    email: EmailStr = Field(..., description="Vendor's email address")
    phone: Optional[str] = Field(None, max_length=20, description="Vendor's phone number")
    address: Optional[str] = Field(None, max_length=200, description="Vendor's address")
    website: Optional[str] = Field(None, max_length=50, description="Vendor's website")
    city: Optional[str] = Field(None, max_length=50, description="Vendor's city")
    state: Optional[str] = Field(None, max_length=50, description="Vendor's state/province")
    postal_code: Optional[str] = Field(None, max_length=20, description="Postal/ZIP code")
    country: Optional[str] = Field(None, max_length=50, description="Vendor's country")

class VendorCreate(VendorBase):
    pass

class VendorUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100, description="Vendor's name")
    email: Optional[EmailStr] = Field(None, description="Vendor's email address")
    phone: Optional[str] = Field(None, max_length=20, description="Vendor's phone number")
    address: Optional[str] = Field(None, max_length=200, description="Vendor's address")
    website: Optional[str] = Field(None, max_length=50, description="Vendor's website")
    city: Optional[str] = Field(None, max_length=50, description="Vendor's city")
    state: Optional[str] = Field(None, max_length=50, description="Vendor's state/province")
    postal_code: Optional[str] = Field(None, max_length=20, description="Postal/ZIP code")
    country: Optional[str] = Field(None, max_length=50, description="Vendor's country")
    active: Optional[bool] = Field(None, description="Whether the vendor is active")

class Vendor(VendorBase):
    id: int
    created_at: datetime
    updated_at: datetime
    active: bool

    class Config:
        from_attributes = True
