from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.session import get_db
from .service import create_roof_component, get_roof_component, update_roof_component, delete_roof_component
from .schemas import RoofComponentCreate, RoofComponentUpdate, RoofComponentInDB

router = APIRouter(prefix="/roof-components", tags=["roof_components"])

@router.post("/", response_model=RoofComponentInDB)
def create_roof_component_route(obj_in: RoofComponentCreate, db: Session = Depends(get_db)):
    return create_roof_component(db, obj_in)

@router.get("/{roof_id}/{product_id}", response_model=RoofComponentInDB)
def get_roof_component_route(roof_id: int, product_id: int, db: Session = Depends(get_db)):
    db_obj = get_roof_component(db, roof_id, product_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="RoofComponent not found")
    return db_obj

@router.put("/{roof_id}/{product_id}", response_model=RoofComponentInDB)
def update_roof_component_route(roof_id: int, product_id: int, obj_in: RoofComponentUpdate, db: Session = Depends(get_db)):
    db_obj = update_roof_component(db, roof_id, product_id, obj_in)
    if not db_obj:
        raise HTTPException(status_code=404, detail="RoofComponent not found")
    return db_obj

@router.delete("/{roof_id}/{product_id}", response_model=RoofComponentInDB)
def delete_roof_component_route(roof_id: int, product_id: int, db: Session = Depends(get_db)):
    db_obj = delete_roof_component(db, roof_id, product_id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="RoofComponent not found")
    return db_obj
