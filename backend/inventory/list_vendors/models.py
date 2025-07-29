from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from backend.db.base import Base
from datetime import datetime

class ListVendors(Base):
    __tablename__ = "list_vendors"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    phone = Column(String(20))
    address = Column(String(200))
    website = Column(String(50))
    city = Column(String(50))
    state = Column(String(50))
    postal_code = Column(String(20))
    country = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    active = Column(Boolean, default=True)

    # Relationship with Component (many-to-many through product_vendor)
    products = relationship(
        "inventory.models.Component", 
        secondary="product_vendor", 
        back_populates="vendors"
    )
    
    # Relationship with ProductVendor for additional attributes in the association table
    vendor_products = relationship(
        "inventory.models.ProductVendor",
        back_populates="vendor"
    )
