from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .service import get_puerta_components, get_puerta_component, create_puerta_component, update_puerta_component, delete_puerta_component
from .schemas import PuertaComponentCreate, PuertaComponentUpdate, PuertaComponentOut
from backend.db.session import get_db

router = APIRouter(prefix="/puerta-component", tags=["PuertaComponent"])

@router.get("/", response_model=list[PuertaComponentOut])
def read_puerta_components(db: Session = Depends(get_db)):
    return get_puerta_components(db)

@router.get("/{puerta_id}/{product_id}", response_model=PuertaComponentOut)
def read_puerta_component(puerta_id: int, product_id: int, db: Session = Depends(get_db)):
    pc = get_puerta_component(db, puerta_id, product_id)
    if not pc:
        raise HTTPException(status_code=404, detail="PuertaComponent not found")
    return pc

@router.post("/", response_model=PuertaComponentOut)
def create_new_puerta_component(data: PuertaComponentCreate, db: Session = Depends(get_db)):
    return create_puerta_component(db, data.dict())

@router.put("/{puerta_id}/{product_id}", response_model=PuertaComponentOut)
def update_existing_puerta_component(puerta_id: int, product_id: int, data: PuertaComponentUpdate, db: Session = Depends(get_db)):
    return update_puerta_component(db, puerta_id, product_id, data.dict())

@router.delete("/{puerta_id}/{product_id}")
def delete_existing_puerta_component(puerta_id: int, product_id: int, db: Session = Depends(get_db)):
    delete_puerta_component(db, puerta_id, product_id)
    return {"detail": "Deleted"}
