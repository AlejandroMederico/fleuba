from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .service import get_gabinetes, get_gabinete, create_gabinete, update_gabinete, delete_gabinete
from .schemas import GabinetesCreate, GabinetesUpdate, GabinetesOut
from backend.db.session import get_db

router = APIRouter(prefix="/gabinetes", tags=["Gabinetes"])

@router.get("/", response_model=list[GabinetesOut])
def read_gabinetes(db: Session = Depends(get_db)):
    return get_gabinetes(db)

@router.get("/{gabinete_id}", response_model=GabinetesOut)
def read_gabinete(gabinete_id: int, db: Session = Depends(get_db)):
    gabinete = get_gabinete(db, gabinete_id)
    if not gabinete:
        raise HTTPException(status_code=404, detail="Gabinete not found")
    return gabinete

@router.post("/", response_model=GabinetesOut)
def create_new_gabinete(gabinete: GabinetesCreate, db: Session = Depends(get_db)):
    return create_gabinete(db, gabinete.dict())

@router.put("/{gabinete_id}", response_model=GabinetesOut)
def update_existing_gabinete(gabinete_id: int, gabinete: GabinetesUpdate, db: Session = Depends(get_db)):
    return update_gabinete(db, gabinete_id, gabinete.dict())

@router.delete("/{gabinete_id}")
def delete_existing_gabinete(gabinete_id: int, db: Session = Depends(get_db)):
    delete_gabinete(db, gabinete_id)
    return {"detail": "Deleted"}
