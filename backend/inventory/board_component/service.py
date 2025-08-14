from sqlalchemy.orm import Session
from .models import BoardComponent
from .schemas import BoardComponentCreate, BoardComponentUpdate

def create_board_component(db: Session, obj_in: BoardComponentCreate):
    db_obj = BoardComponent(**obj_in.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_board_component(db: Session, board_id: int, product_id: int):
    return db.query(BoardComponent).filter_by(board_id=board_id, product_id=product_id).first()

def update_board_component(db: Session, board_id: int, product_id: int, obj_in: BoardComponentUpdate):
    db_obj = get_board_component(db, board_id, product_id)
    if db_obj:
        for field, value in obj_in.dict(exclude_unset=True).items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
    return db_obj

def delete_board_component(db: Session, board_id: int, product_id: int):
    db_obj = get_board_component(db, board_id, product_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()
    return db_obj
