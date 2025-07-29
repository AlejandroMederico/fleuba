from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from backend.db.session import get_db
from . import schemas, service, models

router = APIRouter(prefix="/ivas", tags=["ivas"])

@router.post("/", response_model=schemas.ListIva, status_code=status.HTTP_201_CREATED)
def create_iva(
    iva: schemas.ListIvaCreate, 
    db: Session = Depends(get_db)
):
    """
    Create a new IVA rate.
    """
    return service.create_iva(db=db, iva=iva)

@router.get("/", response_model=List[schemas.ListIva])
def read_ivas(
    skip: int = 0, 
    limit: int = 100, 
    active_only: bool = True,
    db: Session = Depends(get_db)
):
    """
    Retrieve IVA rates. Can be filtered by active status.
    """
    return service.get_all_ivas(
        db, skip=skip, limit=limit, active_only=active_only
    )

@router.get("/{iva_id}", response_model=schemas.ListIva)
def read_iva(iva_id: int, db: Session = Depends(get_db)):
    """
    Get a specific IVA rate by ID.
    """
    db_iva = service.get_iva(db, iva_id=iva_id)
    if db_iva is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="IVA rate not found"
        )
    return db_iva

@router.put("/{iva_id}", response_model=schemas.ListIva)
def update_iva(
    iva_id: int, 
    iva: schemas.ListIvaUpdate, 
    db: Session = Depends(get_db)
):
    """
    Update an IVA rate.
    """
    db_iva = service.get_iva(db, iva_id=iva_id)
    if db_iva is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="IVA rate not found"
        )
    return service.update_iva(
        db=db, db_iva=db_iva, iva=iva
    )

@router.delete("/{iva_id}", response_model=schemas.ListIva)
def delete_iva(iva_id: int, db: Session = Depends(get_db)):
    """
    Delete an IVA rate (soft delete).
    """
    db_iva = service.get_iva(db, iva_id=iva_id)
    if db_iva is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="IVA rate not found"
        )
    return service.delete_iva(db=db, db_iva=db_iva)
