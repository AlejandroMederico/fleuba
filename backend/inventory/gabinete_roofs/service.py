from .models import GabineteRoofs
from sqlalchemy.orm import Session

def get_gabinete_roofs(db: Session):
    return db.query(GabineteRoofs).all()

def get_gabinete_roof(db: Session, gabinete_id: int, roof_id: int):
    return db.query(GabineteRoofs).filter_by(gabinete_id=gabinete_id, roof_id=roof_id).first()

def create_gabinete_roof(db: Session, data):
    gr = GabineteRoofs(**data)
    db.add(gr)
    db.commit()
    db.refresh(gr)
    return gr

def update_gabinete_roof(db: Session, gabinete_id: int, roof_id: int, data):
    gr = get_gabinete_roof(db, gabinete_id, roof_id)
    for key, value in data.items():
        setattr(gr, key, value)
    db.commit()
    db.refresh(gr)
    return gr

def delete_gabinete_roof(db: Session, gabinete_id: int, roof_id: int):
    gr = get_gabinete_roof(db, gabinete_id, roof_id)
    db.delete(gr)
    db.commit()
