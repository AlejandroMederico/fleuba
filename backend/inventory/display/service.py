from sqlalchemy.orm import Session
from .models import Display
from .schemas import DisplayCreate, DisplayUpdate


def create_display(db: Session, obj_in: DisplayCreate):
    db_obj = Display(**obj_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_display(db: Session, display_id: int):
    return db.query(Display).filter_by(id=display_id).first()


def update_display(db: Session, display_id: int, obj_in: DisplayUpdate):
    db_obj = get_display(db, display_id)
    if db_obj:
        for field, value in obj_in.dict(exclude_unset=True).items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj


def delete_display(db: Session, display_id: int):
    db_obj = get_display(db, display_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj
