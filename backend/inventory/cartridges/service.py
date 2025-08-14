from sqlalchemy.orm import Session
from . import models, schemas

def get_cartridge(db: Session, cartridge_id: int):
    return db.query(models.Cartridges).filter(models.Cartridges.id == cartridge_id).first()

def get_cartridges(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cartridges).offset(skip).limit(limit).all()

def create_cartridge(db: Session, cartridge: schemas.CartridgesCreate):
    db_obj = models.Cartridges(**cartridge.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_cartridge(db: Session, db_obj: models.Cartridges, obj_in: schemas.CartridgesUpdate):
    update_data = obj_in.dict(exclude_unset=True)
    for field in update_data:
        if hasattr(db_obj, field):
            setattr(db_obj, field, update_data[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def remove_cartridge(db: Session, cartridge_id: int):
    db_obj = db.query(models.Cartridges).get(cartridge_id)
    db.delete(db_obj)
    db.commit()
    return db_obj
