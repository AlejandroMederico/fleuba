from sqlalchemy.orm import Session
from . import models, schemas

def get_cartridge_electronic_card(db: Session, cartridge_id: int, card_id: int):
    return db.query(models.CartridgeElectronicCards).filter(
        models.CartridgeElectronicCards.cartridge_id == cartridge_id,
        models.CartridgeElectronicCards.card_id == card_id
    ).first()

def get_cartridge_electronic_cards(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CartridgeElectronicCards).offset(skip).limit(limit).all()

def create_cartridge_electronic_card(db: Session, obj_in: schemas.CartridgeElectronicCardsCreate):
    db_obj = models.CartridgeElectronicCards(**obj_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_cartridge_electronic_card(db: Session, cartridge_id: int, card_id: int, obj_in: schemas.CartridgeElectronicCardsUpdate):
    db_obj = get_cartridge_electronic_card(db, cartridge_id, card_id)
    if db_obj is None:
        return None
    update_data = obj_in.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def remove_cartridge_electronic_card(db: Session, cartridge_id: int, card_id: int):
    db_obj = get_cartridge_electronic_card(db, cartridge_id, card_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj
