from .models import GabineteDisplays
from sqlalchemy.orm import Session

def get_gabinete_displays(db: Session):
    return db.query(GabineteDisplays).all()

def get_gabinete_display(db: Session, gabinete_id: int, display_id: int):
    return db.query(GabineteDisplays).filter_by(gabinete_id=gabinete_id, display_id=display_id).first()

def create_gabinete_display(db: Session, data):
    gd = GabineteDisplays(**data)
    db.add(gd)
    db.commit()
    db.refresh(gd)
    return gd

def update_gabinete_display(db: Session, gabinete_id: int, display_id: int, data):
    gd = get_gabinete_display(db, gabinete_id, display_id)
    for key, value in data.items():
        setattr(gd, key, value)
    db.commit()
    db.refresh(gd)
    return gd

def delete_gabinete_display(db: Session, gabinete_id: int, display_id: int):
    gd = get_gabinete_display(db, gabinete_id, display_id)
    db.delete(gd)
    db.commit()
