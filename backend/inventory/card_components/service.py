from sqlalchemy.orm import Session
from . import models, schemas


def get_card_component(db: Session, card_id: int, product_id: int):
    return db.query(models.CardComponent).filter(
        models.CardComponent.card_id == card_id,
        models.CardComponent.product_id == product_id
    ).first()


def get_card_components(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CardComponent).offset(skip).limit(limit).all()


def create_card_component(db: Session, card_component: schemas.CardComponentCreate):
    db_obj = models.CardComponent(**card_component.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_card_component(db: Session, card_id: int, product_id: int, card_component: schemas.CardComponentUpdate):
    db_obj = get_card_component(db, card_id, product_id)
    if db_obj is None:
        return None
    update_data = card_component.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def remove_card_component(db: Session, card_id: int, product_id: int):
    db_obj = get_card_component(db, card_id, product_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj
