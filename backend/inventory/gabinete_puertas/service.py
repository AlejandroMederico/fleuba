
from .models import GabinetePuertas
from sqlalchemy.orm import Session

def get_gabinete_puertas(db: Session):
    return db.query(GabinetePuertas).all()

def get_gabinete_puerta(db: Session, gabinete_id: int, puerta_id: int):
    return db.query(GabinetePuertas).filter_by(gabinete_id=gabinete_id, puerta_id=puerta_id).first()

def create_gabinete_puerta(db: Session, data):
    gp = GabinetePuertas(**data)
    db.add(gp)
    db.commit()
    db.refresh(gp)
    return gp

def update_gabinete_puerta(db: Session, gabinete_id: int, puerta_id: int, data):
    gp = get_gabinete_puerta(db, gabinete_id, puerta_id)
    for key, value in data.items():
        setattr(gp, key, value)
    db.commit()
    db.refresh(gp)
    return gp

def delete_gabinete_puerta(db: Session, gabinete_id: int, puerta_id: int):
    gp = get_gabinete_puerta(db, gabinete_id, puerta_id)
    db.delete(gp)
    db.commit()
