from sqlalchemy.orm import Session
from typing import List, Optional
from . import models, schemas

def get_vendor(db: Session, vendor_id: int) -> Optional[models.ListVendors]:
    """Retrieve a vendor by its ID."""
    return db.query(models.ListVendors).filter(
        models.ListVendors.id == vendor_id,
        models.ListVendors.active == True
    ).first()

def get_vendors(
    db: Session, 
    skip: int = 0, 
    limit: int = 100,
    active_only: bool = True
) -> List[models.ListVendors]:
    """Retrieve a list of vendors, optionally filtered by active status."""
    query = db.query(models.ListVendors)
    if active_only:
        query = query.filter(models.ListVendors.active == True)
    return query.offset(skip).limit(limit).all()

def create_vendor(db: Session, vendor: schemas.VendorCreate) -> models.ListVendors:
    """Create a new vendor."""
    db_vendor = models.ListVendors(**vendor.model_dump())
    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    return db_vendor

def update_vendor(
    db: Session, 
    db_vendor: models.ListVendors, 
    vendor: schemas.VendorUpdate
) -> models.ListVendors:
    """Update an existing vendor."""
    update_data = vendor.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_vendor, field, value)
    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    return db_vendor

def delete_vendor(db: Session, db_vendor: models.ListVendors) -> models.ListVendors:
    """Perform a soft delete of a vendor."""
    db_vendor.active = False
    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    return db_vendor

def get_vendor_products(
    db: Session, 
    vendor_id: int,
    skip: int = 0, 
    limit: int = 100
) -> List[models.ListVendors]:
    """Retrieve all products associated with a specific vendor."""
    vendor = get_vendor(db, vendor_id)
    if not vendor:
        return []
    return vendor.products.offset(skip).limit(limit).all()
