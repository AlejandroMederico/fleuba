from sqlalchemy.orm import Session
from . import models, schemas

def get_cartridge_component(db: Session, cartridge_id: int, product_id: int):
    return db.query(models.CartridgeComponent).filter(
        models.CartridgeComponent.cartridge_id == cartridge_id,
        models.CartridgeComponent.product_id == product_id
    ).first()

def get_cartridge_components(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CartridgeComponent).offset(skip).limit(limit).all()

def create_cartridge_component(db: Session, cartridge_component: schemas.CartridgeComponentCreate):
    db_obj = models.CartridgeComponent(**cartridge_component.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_cartridge_component(db: Session, cartridge_id: int, product_id: int, cartridge_component: schemas.CartridgeComponentUpdate):
    db_obj = get_cartridge_component(db, cartridge_id, product_id)
    if db_obj is None:
        return None
    update_data = cartridge_component.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def remove_cartridge_component(db: Session, cartridge_id: int, product_id: int):
    db_obj = get_cartridge_component(db, cartridge_id, product_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj
