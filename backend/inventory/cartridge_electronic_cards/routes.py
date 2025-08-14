from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import service, schemas
from backend.db.session import get_db

router = APIRouter(prefix="/cartridge_electronic_cards", tags=["cartridge_electronic_cards"])

@router.get("/", response_model=List[schemas.CartridgeElectronicCards])
def read_cartridge_electronic_cards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_cartridge_electronic_cards(db, skip=skip, limit=limit)

@router.get("/{cartridge_id}/{card_id}", response_model=schemas.CartridgeElectronicCards)
def read_cartridge_electronic_card(cartridge_id: int, card_id: int, db: Session = Depends(get_db)):
    obj = service.get_cartridge_electronic_card(db, cartridge_id, card_id)
    if obj is None:
        raise HTTPException(status_code=404, detail="CartridgeElectronicCards not found")
    return obj

@router.post("/", response_model=schemas.CartridgeElectronicCards, status_code=status.HTTP_201_CREATED)
def create_cartridge_electronic_card(obj_in: schemas.CartridgeElectronicCardsCreate, db: Session = Depends(get_db)):
    return service.create_cartridge_electronic_card(db, obj_in)

@router.put("/{cartridge_id}/{card_id}", response_model=schemas.CartridgeElectronicCards)
def update_cartridge_electronic_card(cartridge_id: int, card_id: int, obj_in: schemas.CartridgeElectronicCardsUpdate, db: Session = Depends(get_db)):
    obj = service.get_cartridge_electronic_card(db, cartridge_id, card_id)
    if obj is None:
        raise HTTPException(status_code=404, detail="CartridgeElectronicCards not found")
    return service.update_cartridge_electronic_card(db, cartridge_id, card_id, obj_in)

@router.delete("/{cartridge_id}/{card_id}", response_model=schemas.CartridgeElectronicCards)
def delete_cartridge_electronic_card(cartridge_id: int, card_id: int, db: Session = Depends(get_db)):
    obj = service.get_cartridge_electronic_card(db, cartridge_id, card_id)
    if obj is None:
        raise HTTPException(status_code=404, detail="CartridgeElectronicCards not found")
    return service.remove_cartridge_electronic_card(db, cartridge_id, card_id)
