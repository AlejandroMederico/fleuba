from sqlalchemy.orm import Session
from .models import Roofs
from .schemas import RoofsCreate, RoofsUpdate

def create_roof(db: Session, obj_in: RoofsCreate):
    db_obj = Roofs(**obj_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_roof(db: Session, roof_id: int):
    return db.query(Roofs).filter_by(id=roof_id).first()

def update_roof(db: Session, roof_id: int, obj_in: RoofsUpdate):
    db_obj = get_roof(db, roof_id)
    if db_obj:
        for field, value in obj_in.dict(exclude_unset=True).items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_roof(db: Session, roof_id: int):
    db_obj = get_roof(db, roof_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj
