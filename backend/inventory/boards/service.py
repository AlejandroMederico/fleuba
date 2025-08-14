from sqlalchemy.orm import Session
from . import models, schemas

def get_board(db: Session, board_id: int):
    return db.query(models.Boards).filter(models.Boards.id == board_id).first()

def get_boards(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Boards).offset(skip).limit(limit).all()

def create_board(db: Session, board: schemas.BoardsCreate):
    db_obj = models.Boards(**board.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_board(db: Session, db_obj: models.Boards, obj_in: schemas.BoardsUpdate):
    update_data = obj_in.dict(exclude_unset=True)
    for field in update_data:
        if hasattr(db_obj, field):
            setattr(db_obj, field, update_data[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def remove_board(db: Session, board_id: int):
    db_obj = db.query(models.Boards).get(board_id)
    db.delete(db_obj)
    db.commit()
    return db_obj
