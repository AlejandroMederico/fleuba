from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from . import service, schemas
from backend.db.session import get_db

router = APIRouter(prefix="/card_components", tags=["card_components"])


@router.get("/", response_model=List[schemas.CardComponent])
def read_card_components(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_card_components(db, skip=skip, limit=limit)


@router.get("/{card_id}/{product_id}", response_model=schemas.CardComponent)
def read_card_component(card_id: int, product_id: int, db: Session = Depends(get_db)):
    cc = service.get_card_component(db, card_id, product_id)
    if cc is None:
        raise HTTPException(status_code=404, detail="CardComponent not found")
    return cc


@router.post("/", response_model=schemas.CardComponent, status_code=status.HTTP_201_CREATED)
def create_card_component(card_component: schemas.CardComponentCreate, db: Session = Depends(get_db)):
    return service.create_card_component(db, card_component)


@router.put("/{card_id}/{product_id}", response_model=schemas.CardComponent)
def update_card_component(card_id: int, product_id: int, card_component: schemas.CardComponentUpdate, db: Session = Depends(get_db)):
    cc = service.get_card_component(db, card_id, product_id)
    if cc is None:
        raise HTTPException(status_code=404, detail="CardComponent not found")
    return service.update_card_component(db, card_id, product_id, card_component)


@router.delete("/{card_id}/{product_id}", response_model=schemas.CardComponent)
def delete_card_component(card_id: int, product_id: int, db: Session = Depends(get_db)):
    cc = service.get_card_component(db, card_id, product_id)
    if cc is None:
        raise HTTPException(status_code=404, detail="CardComponent not found")
    return service.remove_card_component(db, card_id, product_id)
