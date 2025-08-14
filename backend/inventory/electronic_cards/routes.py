from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from . import service, schemas
from backend.db.session import get_db

# Se declara el router con el prefijo y etiquetas correspondientes
router = APIRouter(prefix="/electronic_cards", tags=["electronic_cards"])


@router.get("/", response_model=List[schemas.ElectronicCard])
def read_electronic_cards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_electronic_cards(db, skip=skip, limit=limit)


@router.get("/{electronic_card_id}", response_model=schemas.ElectronicCard)
def read_electronic_card(electronic_card_id: int, db: Session = Depends(get_db)):
    electronic_card = service.get_electronic_card(db, electronic_card_id)
    if electronic_card is None:
        raise HTTPException(status_code=404, detail="Electronic card not found")
    return electronic_card


@router.post("/", response_model=schemas.ElectronicCard, status_code=status.HTTP_201_CREATED)
def create_electronic_card(electronic_card: schemas.ElectronicCardCreate, db: Session = Depends(get_db)):
    return service.create_electronic_card(db, electronic_card)


@router.put("/{electronic_card_id}", response_model=schemas.ElectronicCard)
def update_electronic_card(electronic_card_id: int, electronic_card: schemas.ElectronicCardUpdate, db: Session = Depends(get_db)):
    electronic_card_db = service.get_electronic_card(db, electronic_card_id)
    if electronic_card_db is None:
        raise HTTPException(status_code=404, detail="Electronic card not found")
    return service.update_electronic_card(db, electronic_card_db, electronic_card)


@router.delete("/{electronic_card_id}", response_model=schemas.ElectronicCard)
def delete_electronic_card(electronic_card_id: int, db: Session = Depends(get_db)):
    electronic_card_db = service.get_electronic_card(db, electronic_card_id)
    if electronic_card_db is None:
        raise HTTPException(status_code=404, detail="Electronic card not found")
    return service.remove_electronic_card(db, electronic_card_id)
