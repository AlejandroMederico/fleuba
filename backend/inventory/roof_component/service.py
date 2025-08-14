from sqlalchemy.orm import Session
from .models import RoofComponent
from .schemas import RoofComponentCreate, RoofComponentUpdate

def create_roof_component(db: Session, obj_in: RoofComponentCreate):
    db_obj = RoofComponent(**obj_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_roof_component(db: Session, roof_id: int, product_id: int):
    return db.query(RoofComponent).filter_by(roof_id=roof_id, product_id=product_id).first()

def update_roof_component(db: Session, roof_id: int, product_id: int, obj_in: RoofComponentUpdate):
    db_obj = get_roof_component(db, roof_id, product_id)
    if db_obj:
        for field, value in obj_in.dict(exclude_unset=True).items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_roof_component(db: Session, roof_id: int, product_id: int):
    db_obj = get_roof_component(db, roof_id, product_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj
