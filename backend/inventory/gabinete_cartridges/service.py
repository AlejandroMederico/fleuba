from .models import GabineteCartridges
from sqlalchemy.orm import Session

def get_gabinete_cartridges(db: Session):
    return db.query(GabineteCartridges).all()

def get_gabinete_cartridge(db: Session, gabinete_id: int, cartridge_id: int):
    return db.query(GabineteCartridges).filter_by(gabinete_id=gabinete_id, cartridge_id=cartridge_id).first()

def create_gabinete_cartridge(db: Session, data):
    gc = GabineteCartridges(**data)
    db.add(gc)
    db.commit()
    db.refresh(gc)
    return gc

def update_gabinete_cartridge(db: Session, gabinete_id: int, cartridge_id: int, data):
    gc = get_gabinete_cartridge(db, gabinete_id, cartridge_id)
    for key, value in data.items():
        setattr(gc, key, value)
    db.commit()
    db.refresh(gc)
    return gc

def delete_gabinete_cartridge(db: Session, gabinete_id: int, cartridge_id: int):
    gc = get_gabinete_cartridge(db, gabinete_id, cartridge_id)
    db.delete(gc)
    db.commit()
