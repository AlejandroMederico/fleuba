from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import service, schemas
from backend.db.session import get_db

router = APIRouter(prefix="/boards", tags=["boards"])

@router.get("/", response_model=List[schemas.Boards])
def read_boards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_boards(db, skip=skip, limit=limit)

@router.get("/{board_id}", response_model=schemas.Boards)
def read_board(board_id: int, db: Session = Depends(get_db)):
    db_obj = service.get_board(db, board_id)
    if db_obj is None:
        raise HTTPException(status_code=404, detail="Board not found")
    return db_obj

@router.post("/", response_model=schemas.Boards, status_code=status.HTTP_201_CREATED)
def create_board(board: schemas.BoardsCreate, db: Session = Depends(get_db)):
    return service.create_board(db, board)

@router.put("/{board_id}", response_model=schemas.Boards)
def update_board(board_id: int, board: schemas.BoardsUpdate, db: Session = Depends(get_db)):
    db_obj = service.get_board(db, board_id)
    if db_obj is None:
        raise HTTPException(status_code=404, detail="Board not found")
    return service.update_board(db, db_obj, board)

@router.delete("/{board_id}", response_model=schemas.Boards)
def delete_board(board_id: int, db: Session = Depends(get_db)):
    db_obj = service.get_board(db, board_id)
    if db_obj is None:
        raise HTTPException(status_code=404, detail="Board not found")
    return service.remove_board(db, board_id)
