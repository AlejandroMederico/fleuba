from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.session import get_db
from .service import create_roof, get_roof, update_roof, delete_roof
from .schemas import RoofsCreate, RoofsUpdate, RoofsInDB

router = APIRouter(prefix="/roofs", tags=["roofs"])

@router.post("/", response_model=RoofsInDB)
def create_roof_route(obj_in: RoofsCreate, db: Session = Depends(get_db)):
    return create_roof(db, obj_in)

@router.get("/{roof_id}", response_model=RoofsInDB)
def get_roof_route(roof_id: int, db: Session = Depends(get_db)):
    db_obj = get_roof(db, roof_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Roof not found")
    return db_obj

@router.put("/{roof_id}", response_model=RoofsInDB)
def update_roof_route(roof_id: int, obj_in: RoofsUpdate, db: Session = Depends(get_db)):
    db_obj = update_roof(db, roof_id, obj_in)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Roof not found")
    return db_obj

@router.delete("/{roof_id}", response_model=RoofsInDB)
def delete_roof_route(roof_id: int, db: Session = Depends(get_db)):
    db_obj = delete_roof(db, roof_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Roof not found")
    return db_obj
