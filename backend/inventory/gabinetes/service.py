from .models import Gabinetes
from sqlalchemy.orm import Session

def get_gabinetes(db: Session):
    return db.query(Gabinetes).all()

def get_gabinete(db: Session, gabinete_id: int):
    return db.query(Gabinetes).filter(Gabinetes.id == gabinete_id).first()

def create_gabinete(db: Session, gabinete_data):
    gabinete = Gabinetes(**gabinete_data)
    db.add(gabinete)
    db.commit()
    db.refresh(gabinete)
    return gabinete

def update_gabinete(db: Session, gabinete_id: int, gabinete_data):
    gabinete = get_gabinete(db, gabinete_id)
    for key, value in gabinete_data.items():
        setattr(gabinete, key, value)
    db.commit()
    db.refresh(gabinete)
    return gabinete

def delete_gabinete(db: Session, gabinete_id: int):
    gabinete = get_gabinete(db, gabinete_id)
    db.delete(gabinete)
    db.commit()
