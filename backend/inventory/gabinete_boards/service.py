from .models import GabineteBoards
from sqlalchemy.orm import Session

def get_gabinete_boards(db: Session):
    return db.query(GabineteBoards).all()

def get_gabinete_board(db: Session, gabinete_id: int, board_id: int):
    return db.query(GabineteBoards).filter_by(gabinete_id=gabinete_id, board_id=board_id).first()

def create_gabinete_board(db: Session, data):
    gb = GabineteBoards(**data)
    db.add(gb)
    db.commit()
    db.refresh(gb)
    return gb

def update_gabinete_board(db: Session, gabinete_id: int, board_id: int, data):
    gb = get_gabinete_board(db, gabinete_id, board_id)
    for key, value in data.items():
        setattr(gb, key, value)
    db.commit()
    db.refresh(gb)
    return gb

def delete_gabinete_board(db: Session, gabinete_id: int, board_id: int):
    gb = get_gabinete_board(db, gabinete_id, board_id)
    db.delete(gb)
    db.commit()
