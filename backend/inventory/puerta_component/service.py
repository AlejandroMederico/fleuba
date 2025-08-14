from .models import PuertaComponent
from sqlalchemy.orm import Session


def get_puerta_components(db: Session):
    return db.query(PuertaComponent).all()


def get_puerta_component(db: Session, puerta_id: int, product_id: int):
    return (
        db.query(PuertaComponent)
        .filter_by(puerta_id=puerta_id, product_id=product_id)
        .first()
    )


def create_puerta_component(db: Session, data):
    pc = PuertaComponent(**data)
    db.add(pc)
    db.commit()
    db.refresh(pc)
    return pc


def update_puerta_component(db: Session, puerta_id: int, product_id: int, data):
    pc = get_puerta_component(db, puerta_id, product_id)
    for key, value in data.items():
        setattr(pc, key, value)
    db.commit()
    db.refresh(pc)
    return pc


def delete_puerta_component(db: Session, puerta_id: int, product_id: int):
    pc = get_puerta_component(db, puerta_id, product_id)
    db.delete(pc)
    db.commit()
