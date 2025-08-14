from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.session import get_db
from .service import create_board_component, get_board_component, update_board_component, delete_board_component
from .schemas import BoardComponentCreate, BoardComponentUpdate, BoardComponentInDB

router = APIRouter(prefix="/board-components", tags=["board_components"])

@router.post("/", response_model=BoardComponentInDB)
def create_board_component_route(obj_in: BoardComponentCreate, db: Session = Depends(get_db)):
    return create_board_component(db, obj_in)

@router.get("/{board_id}/{product_id}", response_model=BoardComponentInDB)
def get_board_component_route(board_id: int, product_id: int, db: Session = Depends(get_db)):
    db_obj = get_board_component(db, board_id, product_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="BoardComponent not found")
    return db_obj

@router.put("/{board_id}/{product_id}", response_model=BoardComponentInDB)
def update_board_component_route(board_id: int, product_id: int, obj_in: BoardComponentUpdate, db: Session = Depends(get_db)):
    db_obj = update_board_component(db, board_id, product_id, obj_in)
    if not db_obj:
        raise HTTPException(status_code=404, detail="BoardComponent not found")
    return db_obj

@router.delete("/{board_id}/{product_id}", response_model=BoardComponentInDB)
def delete_board_component_route(board_id: int, product_id: int, db: Session = Depends(get_db)):
    db_obj = delete_board_component(db, board_id, product_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="BoardComponent not found")
    return db_obj
