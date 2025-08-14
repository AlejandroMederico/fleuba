from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .service import get_gabinete_boards, get_gabinete_board, create_gabinete_board, update_gabinete_board, delete_gabinete_board
from .schemas import GabineteBoardsCreate, GabineteBoardsUpdate, GabineteBoardsOut
from backend.db.session import get_db

router = APIRouter(prefix="/gabinete-boards", tags=["GabineteBoards"])

@router.get("/", response_model=list[GabineteBoardsOut])
def read_gabinete_boards(db: Session = Depends(get_db)):
    return get_gabinete_boards(db)

@router.get("/{gabinete_id}/{board_id}", response_model=GabineteBoardsOut)
def read_gabinete_board(gabinete_id: int, board_id: int, db: Session = Depends(get_db)):
    gb = get_gabinete_board(db, gabinete_id, board_id)
    if not gb:
        raise HTTPException(status_code=404, detail="GabineteBoards not found")
    return gb

@router.post("/", response_model=GabineteBoardsOut)
def create_new_gabinete_board(data: GabineteBoardsCreate, db: Session = Depends(get_db)):
    return create_gabinete_board(db, data.dict())

@router.put("/{gabinete_id}/{board_id}", response_model=GabineteBoardsOut)
def update_existing_gabinete_board(gabinete_id: int, board_id: int, data: GabineteBoardsUpdate, db: Session = Depends(get_db)):
    return update_gabinete_board(db, gabinete_id, board_id, data.dict())

@router.delete("/{gabinete_id}/{board_id}")
def delete_existing_gabinete_board(gabinete_id: int, board_id: int, db: Session = Depends(get_db)):
    delete_gabinete_board(db, gabinete_id, board_id)
    return {"detail": "Deleted"}
