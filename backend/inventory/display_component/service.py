from sqlalchemy.orm import Session
from .models import DisplayComponent
from .schemas import DisplayComponentCreate, DisplayComponentUpdate

def create_display_component(db: Session, obj_in: DisplayComponentCreate):
    db_obj = DisplayComponent(**obj_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_display_component(db: Session, display_id: int, product_id: int):
    return db.query(DisplayComponent).filter_by(display_id=display_id, product_id=product_id).first()

def update_display_component(db: Session, display_id: int, product_id: int, obj_in: DisplayComponentUpdate):
    db_obj = get_display_component(db, display_id, product_id)
    if db_obj:
        for field, value in obj_in.dict(exclude_unset=True).items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_display_component(db: Session, display_id: int, product_id: int):
    db_obj = get_display_component(db, display_id, product_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj
