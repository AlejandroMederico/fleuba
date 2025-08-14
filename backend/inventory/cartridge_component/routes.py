from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import service, schemas
from backend.db.session import get_db

router = APIRouter(prefix="/cartridge_components", tags=["cartridge_components"])

@router.get("/", response_model=List[schemas.CartridgeComponent])
def read_cartridge_components(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_cartridge_components(db, skip=skip, limit=limit)

@router.get("/{cartridge_id}/{product_id}", response_model=schemas.CartridgeComponent)
def read_cartridge_component(cartridge_id: int, product_id: int, db: Session = Depends(get_db)):
    cc = service.get_cartridge_component(db, cartridge_id, product_id)
    if cc is None:
        raise HTTPException(status_code=404, detail="CartridgeComponent not found")
    return cc

@router.post("/", response_model=schemas.CartridgeComponent, status_code=status.HTTP_201_CREATED)
def create_cartridge_component(cartridge_component: schemas.CartridgeComponentCreate, db: Session = Depends(get_db)):
    return service.create_cartridge_component(db, cartridge_component)

@router.put("/{cartridge_id}/{product_id}", response_model=schemas.CartridgeComponent)
def update_cartridge_component(cartridge_id: int, product_id: int, cartridge_component: schemas.CartridgeComponentUpdate, db: Session = Depends(get_db)):
    cc = service.get_cartridge_component(db, cartridge_id, product_id)
    if cc is None:
        raise HTTPException(status_code=404, detail="CartridgeComponent not found")
    return service.update_cartridge_component(db, cartridge_id, product_id, cartridge_component)

@router.delete("/{cartridge_id}/{product_id}", response_model=schemas.CartridgeComponent)
def delete_cartridge_component(cartridge_id: int, product_id: int, db: Session = Depends(get_db)):
    cc = service.get_cartridge_component(db, cartridge_id, product_id)
    if cc is None:
        raise HTTPException(status_code=404, detail="CartridgeComponent not found")
    return service.remove_cartridge_component(db, cartridge_id, product_id)
