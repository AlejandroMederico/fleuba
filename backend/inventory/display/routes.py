from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.session import get_db
from .service import create_display, get_display, update_display, delete_display
from .schemas import DisplayCreate, DisplayUpdate, DisplayInDB

router = APIRouter(prefix="/displays", tags=["displays"])


@router.post("/", response_model=DisplayInDB)
def create_display_route(obj_in: DisplayCreate, db: Session = Depends(get_db)):
    return create_display(db, obj_in)


@router.get("/{display_id}", response_model=DisplayInDB)
def get_display_route(display_id: int, db: Session = Depends(get_db)):
    db_obj = get_display(db, display_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Display not found")
    return db_obj


@router.put("/{display_id}", response_model=DisplayInDB)
def update_display_route(
    display_id: int, obj_in: DisplayUpdate, db: Session = Depends(get_db)
):
    db_obj = update_display(db, display_id, obj_in)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Display not found")
    return db_obj


@router.delete("/{display_id}", response_model=DisplayInDB)
def delete_display_route(display_id: int, db: Session = Depends(get_db)):
    db_obj = delete_display(db, display_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Display not found")
    return db_obj
