from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from . import models, schemas
from inventory.models import Component
from inventory.list_vendors.models import ListVendors

class ProductVendorService:
    @staticmethod
    def get_product_vendor(
        db: Session, 
        product_id: int, 
        vendor_id: int
    ) -> Optional[models.ProductVendor]:
        """Retrieve a specific product-vendor relationship."""
        return db.query(models.ProductVendor).filter(
            models.ProductVendor.product_id == product_id,
            models.ProductVendor.vendor_id == vendor_id
        ).first()

    @staticmethod
    def get_product_vendors(
        db: Session, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[models.ProductVendor]:
        """Retrieve all product-vendor relationships with pagination."""
        return db.query(models.ProductVendor).offset(skip).limit(limit).all()

    @staticmethod
    def get_vendors_for_product(
        db: Session, 
        product_id: int
    ) -> List[models.ProductVendor]:
        """Retrieve all vendors for a specific product."""
        return db.query(models.ProductVendor).filter(
            models.ProductVendor.product_id == product_id
        ).all()

    @staticmethod
    def get_products_for_vendor(
        db: Session, 
        vendor_id: int
    ) -> List[models.ProductVendor]:
        """Retrieve all products for a specific vendor."""
        return db.query(models.ProductVendor).filter(
            models.ProductVendor.vendor_id == vendor_id
        ).all()

    @staticmethod
    def create_product_vendor(
        db: Session, 
        product_vendor: schemas.ProductVendorCreate
    ) -> models.ProductVendor:
        """Create a new product-vendor relationship."""
        # Check if product exists
        db_product = db.query(Component).filter(
            Component.id == product_vendor.product_id
        ).first()
        if not db_product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with id {product_vendor.product_id} not found"
            )
        
        # Check if vendor exists
        db_vendor = db.query(ListVendors).filter(
            ListVendors.id == product_vendor.vendor_id
        ).first()
        if not db_vendor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Vendor with id {product_vendor.vendor_id} not found"
            )
        
        # Check if relationship already exists
        db_product_vendor = ProductVendorService.get_product_vendor(
            db=db,
            product_id=product_vendor.product_id,
            vendor_id=product_vendor.vendor_id
        )
        if db_product_vendor:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This product-vendor relationship already exists"
            )
        
        # Create the relationship
        db_product_vendor = models.ProductVendor(**product_vendor.dict())
        db.add(db_product_vendor)
        db.commit()
        db.refresh(db_product_vendor)
        return db_product_vendor

    @staticmethod
    def update_product_vendor(
        db: Session,
        product_id: int,
        vendor_id: int,
        product_vendor_update: schemas.ProductVendorUpdate
    ) -> models.ProductVendor:
        """Update an existing product-vendor relationship."""
        db_product_vendor = ProductVendorService.get_product_vendor(
            db=db,
            product_id=product_id,
            vendor_id=vendor_id
        )
        
        if not db_product_vendor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product-vendor relationship not found"
            )
        
        # Update fields
        update_data = product_vendor_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_product_vendor, field, value)
        
        db.commit()
        db.refresh(db_product_vendor)
        return db_product_vendor

    @staticmethod
    def delete_product_vendor(
        db: Session, 
        product_id: int, 
        vendor_id: int
    ) -> bool:
        """Delete a product-vendor relationship."""
        db_product_vendor = ProductVendorService.get_product_vendor(
            db=db,
            product_id=product_id,
            vendor_id=vendor_id
        )
        
        if not db_product_vendor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product-vendor relationship not found"
            )
        
        db.delete(db_product_vendor)
        db.commit()
        return True
