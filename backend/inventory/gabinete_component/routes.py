from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .service import get_gabinete_components, get_gabinete_component, create_gabinete_component, update_gabinete_component, delete_gabinete_component
from .schemas import GabineteComponentCreate, GabineteComponentUpdate, GabineteComponentOut
from backend.db.session import get_db

router = APIRouter(prefix="/gabinete-component", tags=["GabineteComponent"])

@router.get("/", response_model=list[GabineteComponentOut])
def read_gabinete_components(db: Session = Depends(get_db)):
    return get_gabinete_components(db)

@router.get("/{gabinete_id}/{product_id}", response_model=GabineteComponentOut)
def read_gabinete_component(gabinete_id: int, product_id: int, db: Session = Depends(get_db)):
    gc = get_gabinete_component(db, gabinete_id, product_id)
    if not gc:
        raise HTTPException(status_code=404, detail="GabineteComponent not found")
    return gc

@router.post("/", response_model=GabineteComponentOut)
def create_new_gabinete_component(data: GabineteComponentCreate, db: Session = Depends(get_db)):
    return create_gabinete_component(db, data.dict())

@router.put("/{gabinete_id}/{product_id}", response_model=GabineteComponentOut)
def update_existing_gabinete_component(gabinete_id: int, product_id: int, data: GabineteComponentUpdate, db: Session = Depends(get_db)):
    return update_gabinete_component(db, gabinete_id, product_id, data.dict())

@router.delete("/{gabinete_id}/{product_id}")
def delete_existing_gabinete_component(gabinete_id: int, product_id: int, db: Session = Depends(get_db)):
    delete_gabinete_component(db, gabinete_id, product_id)
    return {"detail": "Deleted"}
