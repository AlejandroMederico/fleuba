from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from backend.db.session import get_db
from . import schemas, service, models

router = APIRouter(prefix="/subcategories", tags=["subcategories"])

@router.post("/", response_model=schemas.Subcategory, status_code=status.HTTP_201_CREATED)
def create_subcategory(
    subcategory: schemas.SubcategoryCreate, 
    db: Session = Depends(get_db)
):
    """
    Create a new subcategory.
    """
    return service.create_subcategory(db=db, subcategory=subcategory)

@router.get("/", response_model=List[schemas.Subcategory])
def read_subcategories(
    skip: int = 0, 
    limit: int = 100, 
    category_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    """
    Retrieve subcategories. Can be filtered by category_id.
    """
    subcategories = service.get_subcategories(
        db, skip=skip, limit=limit, category_id=category_id
    )
    return subcategories

@router.get("/{subcategory_id}", response_model=schemas.Subcategory)
def read_subcategory(subcategory_id: int, db: Session = Depends(get_db)):
    """
    Get a specific subcategory by ID.
    """
    db_subcategory = service.get_subcategory(db, subcategory_id=subcategory_id)
    if db_subcategory is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Subcategory not found"
        )
    return db_subcategory

@router.put("/{subcategory_id}", response_model=schemas.Subcategory)
def update_subcategory(
    subcategory_id: int, 
    subcategory: schemas.SubcategoryUpdate, 
    db: Session = Depends(get_db)
):
    """
    Update a subcategory.
    """
    db_subcategory = service.get_subcategory(db, subcategory_id=subcategory_id)
    if db_subcategory is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Subcategory not found"
        )
    return service.update_subcategory(
        db=db, db_subcategory=db_subcategory, subcategory=subcategory
    )

@router.delete("/{subcategory_id}", response_model=schemas.Subcategory)
def delete_subcategory(subcategory_id: int, db: Session = Depends(get_db)):
    """
    Delete a subcategory (soft delete).
    """
    db_subcategory = service.get_subcategory(db, subcategory_id=subcategory_id)
    if db_subcategory is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Subcategory not found"
        )
    return service.delete_subcategory(db=db, db_subcategory=db_subcategory)
