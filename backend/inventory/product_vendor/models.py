from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.db.base import Base
from datetime import datetime

class ProductVendor(Base):
    __tablename__ = "product_vendor"
    
    product_id = Column(Integer, ForeignKey("component.id"), primary_key=True)
    vendor_id = Column(Integer, ForeignKey("list_vendors.id"), primary_key=True)
    cost = Column(Float, nullable=False, comment="Cost of the product from this vendor")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    product = relationship("inventory.models.Component", back_populates="product_vendors")
    vendor = relationship("inventory.list_vendors.models.ListVendors", back_populates="vendor_products")
