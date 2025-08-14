from .models import GabineteComponent
from sqlalchemy.orm import Session

def get_gabinete_components(db: Session):
    return db.query(GabineteComponent).all()

def get_gabinete_component(db: Session, gabinete_id: int, product_id: int):
    return db.query(GabineteComponent).filter_by(gabinete_id=gabinete_id, product_id=product_id).first()

def create_gabinete_component(db: Session, data):
    gc = GabineteComponent(**data)
    db.add(gc)
    db.commit()
    db.refresh(gc)
    return gc

def update_gabinete_component(db: Session, gabinete_id: int, product_id: int, data):
    gc = get_gabinete_component(db, gabinete_id, product_id)
    for key, value in data.items():
        setattr(gc, key, value)
    db.commit()
    db.refresh(gc)
    return gc

def delete_gabinete_component(db: Session, gabinete_id: int, product_id: int):
    gc = get_gabinete_component(db, gabinete_id, product_id)
    db.delete(gc)
    db.commit()
