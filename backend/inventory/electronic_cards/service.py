from sqlalchemy.orm import Session
from . import models, schemas

def get_electronic_card(db: Session, electronic_card_id: int):
    return db.query(models.ElectronicCards).filter(models.ElectronicCards.id == electronic_card_id).first()

def get_electronic_cards(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ElectronicCards).offset(skip).limit(limit).all()

def create_electronic_card(db: Session, electronic_card: schemas.ElectronicCardCreate):
    db_electronic_card = models.ElectronicCards(**electronic_card.dict())
    db.add(db_electronic_card)
    db.commit()
    db.refresh(db_electronic_card)
    return db_electronic_card

def update_electronic_card(db: Session, db_obj: models.ElectronicCards, obj_in: schemas.ElectronicCardUpdate):
    if isinstance(obj_in, dict):
        update_data = obj_in
    else:
        update_data = obj_in.dict(exclude_unset=True)
    for field in update_data:
        if hasattr(db_obj, field):
            setattr(db_obj, field, update_data[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def remove_electronic_card(db: Session, id: int):
    db_obj = db.query(models.ElectronicCards).get(id)
    db.delete(db_obj)
    db.commit()
    return db_obj
