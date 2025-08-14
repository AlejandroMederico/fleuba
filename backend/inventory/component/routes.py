from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .service import get_components, get_component, create_component, update_component, delete_component
from .schemas import ComponentCreate, ComponentUpdate, ComponentOut
from backend.db.session import get_db

router = APIRouter(prefix="/component", tags=["Component"])

@router.get("/", response_model=list[ComponentOut])
def read_components(db: Session = Depends(get_db)):
    return get_components(db)

@router.get("/{component_id}", response_model=ComponentOut)
def read_component(component_id: int, db: Session = Depends(get_db)):
    component = get_component(db, component_id)
    if not component:
        raise HTTPException(status_code=404, detail="Component not found")
    return component

@router.post("/", response_model=ComponentOut)
def create_new_component(component: ComponentCreate, db: Session = Depends(get_db)):
    return create_component(db, component.dict())

@router.put("/{component_id}", response_model=ComponentOut)
def update_existing_component(component_id: int, component: ComponentUpdate, db: Session = Depends(get_db)):
    return update_component(db, component_id, component.dict())

@router.delete("/{component_id}")
def delete_existing_component(component_id: int, db: Session = Depends(get_db)):
    delete_component(db, component_id)
    return {"detail": "Deleted"}
