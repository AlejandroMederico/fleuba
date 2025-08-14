from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .service import get_gabinete_electronic_cards, get_gabinete_electronic_card, create_gabinete_electronic_card, update_gabinete_electronic_card, delete_gabinete_electronic_card
from .schemas import GabineteElectronicCardsCreate, GabineteElectronicCardsUpdate, GabineteElectronicCardsOut
from backend.db.session import get_db

router = APIRouter(prefix="/gabinete-electronic-cards", tags=["GabineteElectronicCards"])

@router.get("/", response_model=list[GabineteElectronicCardsOut])
def read_gabinete_electronic_cards(db: Session = Depends(get_db)):
    return get_gabinete_electronic_cards(db)

@router.get("/{gabinete_id}/{electronic_card_id}", response_model=GabineteElectronicCardsOut)
def read_gabinete_electronic_card(gabinete_id: int, electronic_card_id: int, db: Session = Depends(get_db)):
    gec = get_gabinete_electronic_card(db, gabinete_id, electronic_card_id)
    if not gec:
        raise HTTPException(status_code=404, detail="GabineteElectronicCards not found")
    return gec

@router.post("/", response_model=GabineteElectronicCardsOut)
def create_new_gabinete_electronic_card(data: GabineteElectronicCardsCreate, db: Session = Depends(get_db)):
    return create_gabinete_electronic_card(db, data.dict())

@router.put("/{gabinete_id}/{electronic_card_id}", response_model=GabineteElectronicCardsOut)
def update_existing_gabinete_electronic_card(gabinete_id: int, electronic_card_id: int, data: GabineteElectronicCardsUpdate, db: Session = Depends(get_db)):
    return update_gabinete_electronic_card(db, gabinete_id, electronic_card_id, data.dict())

@router.delete("/{gabinete_id}/{electronic_card_id}")
def delete_existing_gabinete_electronic_card(gabinete_id: int, electronic_card_id: int, db: Session = Depends(get_db)):
    delete_gabinete_electronic_card(db, gabinete_id, electronic_card_id)
    return {"detail": "Deleted"}
