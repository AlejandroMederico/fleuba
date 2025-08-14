from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import service, schemas
from backend.db.session import get_db

router = APIRouter(prefix="/cartridges", tags=["cartridges"])

@router.get("/", response_model=List[schemas.Cartridges])
def read_cartridges(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_cartridges(db, skip=skip, limit=limit)

@router.get("/{cartridge_id}", response_model=schemas.Cartridges)
def read_cartridge(cartridge_id: int, db: Session = Depends(get_db)):
    db_obj = service.get_cartridge(db, cartridge_id)
    if db_obj is None:
        raise HTTPException(status_code=404, detail="Cartridge not found")
    return db_obj

@router.post("/", response_model=schemas.Cartridges, status_code=status.HTTP_201_CREATED)
def create_cartridge(cartridge: schemas.CartridgesCreate, db: Session = Depends(get_db)):
    return service.create_cartridge(db, cartridge)

@router.put("/{cartridge_id}", response_model=schemas.Cartridges)
def update_cartridge(cartridge_id: int, cartridge: schemas.CartridgesUpdate, db: Session = Depends(get_db)):
    db_obj = service.get_cartridge(db, cartridge_id)
    if db_obj is None:
        raise HTTPException(status_code=404, detail="Cartridge not found")
    return service.update_cartridge(db, db_obj, cartridge)

@router.delete("/{cartridge_id}", response_model=schemas.Cartridges)
def delete_cartridge(cartridge_id: int, db: Session = Depends(get_db)):
    db_obj = service.get_cartridge(db, cartridge_id)
    if db_obj is None:
        raise HTTPException(status_code=404, detail="Cartridge not found")
    return service.remove_cartridge(db, cartridge_id)
