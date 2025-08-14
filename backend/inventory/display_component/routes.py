from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.session import get_db
from .service import create_display_component, get_display_component, update_display_component, delete_display_component
from .schemas import DisplayComponentCreate, DisplayComponentUpdate, DisplayComponentInDB

router = APIRouter(prefix="/display-components", tags=["display_components"])

@router.post("/", response_model=DisplayComponentInDB)
def create_display_component_route(obj_in: DisplayComponentCreate, db: Session = Depends(get_db)):
    return create_display_component(db, obj_in)

@router.get("/{display_id}/{product_id}", response_model=DisplayComponentInDB)
def get_display_component_route(display_id: int, product_id: int, db: Session = Depends(get_db)):
    db_obj = get_display_component(db, display_id, product_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="DisplayComponent not found")
    return db_obj

@router.put("/{display_id}/{product_id}", response_model=DisplayComponentInDB)
def update_display_component_route(display_id: int, product_id: int, obj_in: DisplayComponentUpdate, db: Session = Depends(get_db)):
    db_obj = update_display_component(db, display_id, product_id, obj_in)
    if not db_obj:
        raise HTTPException(status_code=404, detail="DisplayComponent not found")
    return db_obj

@router.delete("/{display_id}/{product_id}", response_model=DisplayComponentInDB)
def delete_display_component_route(display_id: int, product_id: int, db: Session = Depends(get_db)):
    db_obj = delete_display_component(db, display_id, product_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="DisplayComponent not found")
    return db_obj
