from .models import GabineteElectronicCards
from sqlalchemy.orm import Session

def get_gabinete_electronic_cards(db: Session):
    return db.query(GabineteElectronicCards).all()

def get_gabinete_electronic_card(db: Session, gabinete_id: int, electronic_card_id: int):
    return db.query(GabineteElectronicCards).filter_by(gabinete_id=gabinete_id, electronic_card_id=electronic_card_id).first()

def create_gabinete_electronic_card(db: Session, data):
    gec = GabineteElectronicCards(**data)
    db.add(gec)
    db.commit()
    db.refresh(gec)
    return gec

def update_gabinete_electronic_card(db: Session, gabinete_id: int, electronic_card_id: int, data):
    gec = get_gabinete_electronic_card(db, gabinete_id, electronic_card_id)
    for key, value in data.items():
        setattr(gec, key, value)
    db.commit()
    db.refresh(gec)
    return gec

def delete_gabinete_electronic_card(db: Session, gabinete_id: int, electronic_card_id: int):
    gec = get_gabinete_electronic_card(db, gabinete_id, electronic_card_id)
    db.delete(gec)
    db.commit()
