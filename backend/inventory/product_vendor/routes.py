from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from backend.db.database import get_db
from . import service, schemas
from .models import ProductVendor as ProductVendorModel

router = APIRouter(
    prefix="/product-vendors",
    tags=["product_vendors"],
    responses={404: {"description": "Not found"}},
)

@router.post(
    "/", 
    response_model=schemas.ProductVendor,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new product-vendor relationship"
)
def create_product_vendor(
    product_vendor: schemas.ProductVendorCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new relationship between a product and a vendor with a specific cost.
    """
    return service.ProductVendorService.create_product_vendor(db=db, product_vendor=product_vendor)

@router.get(
    "/", 
    response_model=List[schemas.ProductVendorWithDetails],
    summary="Get all product-vendor relationships"
)
def read_product_vendors(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    """
    Retrieve all product-vendor relationships with pagination.
    """
    return service.ProductVendorService.get_product_vendors(db, skip=skip, limit=limit)

@router.get(
    "/product/{product_id}",
    response_model=List[schemas.ProductVendorWithDetails],
    summary="Get all vendors for a specific product"
)
def read_vendors_for_product(
    product_id: int, 
    db: Session = Depends(get_db)
):
    """
    Retrieve all vendors that supply a specific product.
    """
    return service.ProductVendorService.get_vendors_for_product(db, product_id=product_id)

@router.get(
    "/vendor/{vendor_id}",
    response_model=List[schemas.ProductVendorWithDetails],
    summary="Get all products for a specific vendor"
)
def read_products_for_vendor(
    vendor_id: int, 
    db: Session = Depends(get_db)
):
    """
    Retrieve all products supplied by a specific vendor.
    """
    return service.ProductVendorService.get_products_for_vendor(db, vendor_id=vendor_id)

@router.get(
    "/{product_id}/{vendor_id}",
    response_model=schemas.ProductVendorWithDetails,
    summary="Get a specific product-vendor relationship"
)
def read_product_vendor(
    product_id: int, 
    vendor_id: int, 
    db: Session = Depends(get_db)
):
    """
    Retrieve a specific product-vendor relationship by product ID and vendor ID.
    """
    db_product_vendor = service.ProductVendorService.get_product_vendor(
        db, product_id=product_id, vendor_id=vendor_id
    )
    if db_product_vendor is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Product-vendor relationship not found"
        )
    return db_product_vendor

@router.patch(
    "/{product_id}/{vendor_id}",
    response_model=schemas.ProductVendor,
    summary="Update a product-vendor relationship"
)
def update_product_vendor(
    product_id: int, 
    vendor_id: int, 
    product_vendor_update: schemas.ProductVendorUpdate,
    db: Session = Depends(get_db)
):
    """
    Update the cost or other details of a product-vendor relationship.
    """
    return service.ProductVendorService.update_product_vendor(
        db=db,
        product_id=product_id,
        vendor_id=vendor_id,
        product_vendor_update=product_vendor_update
    )

@router.delete(
    "/{product_id}/{vendor_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a product-vendor relationship"
)
def delete_product_vendor(
    product_id: int, 
    vendor_id: int, 
    db: Session = Depends(get_db)
):
    """
    Delete a product-vendor relationship.
    """
    if not service.ProductVendorService.delete_product_vendor(
        db=db, product_id=product_id, vendor_id=vendor_id
    ):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product-vendor relationship not found"
        )
    return {"ok": True}
