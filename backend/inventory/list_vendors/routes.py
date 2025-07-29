from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from backend.db.session import get_db
from . import schemas, service, models

router = APIRouter(prefix="/vendors", tags=["vendors"])

@router.post("/", response_model=schemas.Vendor, status_code=status.HTTP_201_CREATED)
def create_vendor(
    vendor: schemas.VendorCreate, 
    db: Session = Depends(get_db)
):
    """
    Create a new vendor.
    """
    db_vendor = service.get_vendors(db, skip=0, limit=1, active_only=False)
    if db_vendor and any(v.email == vendor.email for v in db_vendor):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    return service.create_vendor(db=db, vendor=vendor)

@router.get("/", response_model=List[schemas.Vendor])
def read_vendors(
    skip: int = 0, 
    limit: int = 100, 
    active_only: bool = True,
    db: Session = Depends(get_db)
):
    """
    Retrieve vendors. Can be filtered by active status.
    """
    vendors = service.get_vendors(
        db, skip=skip, limit=limit, active_only=active_only
    )
    return vendors

@router.get("/{vendor_id}", response_model=schemas.Vendor)
def read_vendor(vendor_id: int, db: Session = Depends(get_db)):
    """
    Get a specific vendor by ID.
    """
    db_vendor = service.get_vendor(db, vendor_id=vendor_id)
    if db_vendor is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Vendor not found"
        )
    return db_vendor

@router.put("/{vendor_id}", response_model=schemas.Vendor)
def update_vendor(
    vendor_id: int, 
    vendor: schemas.VendorUpdate, 
    db: Session = Depends(get_db)
):
    """
    Update a vendor.
    """
    db_vendor = service.get_vendor(db, vendor_id=vendor_id)
    if db_vendor is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Vendor not found"
        )
    
    # Check if email is being updated and if it's already in use
    if vendor.email and vendor.email != db_vendor.email:
        existing_vendor = db.query(models.ListVendors).filter(
            models.ListVendors.email == vendor.email,
            models.ListVendors.id != vendor_id
        ).first()
        if existing_vendor:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already in use by another vendor"
            )
    
    return service.update_vendor(
        db=db, db_vendor=db_vendor, vendor=vendor
    )

@router.delete("/{vendor_id}", response_model=schemas.Vendor)
def delete_vendor(vendor_id: int, db: Session = Depends(get_db)):
    """
    Delete a vendor (soft delete).
    """
    db_vendor = service.get_vendor(db, vendor_id=vendor_id)
    if db_vendor is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Vendor not found"
        )
    return service.delete_vendor(db=db, db_vendor=db_vendor)

@router.get("/{vendor_id}/products", response_model=List[schemas.Vendor])
def read_vendor_products(
    vendor_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Get all products associated with a specific vendor.
    """
    db_vendor = service.get_vendor(db, vendor_id=vendor_id)
    if db_vendor is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Vendor not found"
        )
    return db_vendor.products.offset(skip).limit(limit).all()
