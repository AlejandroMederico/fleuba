from .models import Puertas
from sqlalchemy.orm import Session


def get_puertas(db: Session):
    return db.query(Puertas).all()


def get_puerta(db: Session, puerta_id: int):
    return db.query(Puertas).filter(Puertas.id == puerta_id).first()


def create_puerta(db: Session, puerta_data):
    puerta = Puertas(**puerta_data)
    db.add(puerta)
    db.commit()
    db.refresh(puerta)
    return puerta


def update_puerta(db: Session, puerta_id: int, puerta_data):
    puerta = get_puerta(db, puerta_id)
    for key, value in puerta_data.items():
        setattr(puerta, key, value)
    db.commit()
    db.refresh(puerta)
    return puerta


def delete_puerta(db: Session, puerta_id: int):
    puerta = get_puerta(db, puerta_id)
    db.delete(puerta)
    db.commit()
