from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .service import get_gabinete_puertas, get_gabinete_puerta, create_gabinete_puerta, update_gabinete_puerta, delete_gabinete_puerta
from .schemas import GabinetePuertasCreate, GabinetePuertasUpdate, GabinetePuertasOut
from backend.db.session import get_db

router = APIRouter(prefix="/gabinete-puertas", tags=["GabinetePuertas"])

@router.get("/", response_model=list[GabinetePuertasOut])
def read_gabinete_puertas(db: Session = Depends(get_db)):
    return get_gabinete_puertas(db)

@router.get("/{gabinete_id}/{puerta_id}", response_model=GabinetePuertasOut)
def read_gabinete_puerta(gabinete_id: int, puerta_id: int, db: Session = Depends(get_db)):
    gp = get_gabinete_puerta(db, gabinete_id, puerta_id)
    if not gp:
        raise HTTPException(status_code=404, detail="GabinetePuertas not found")
    return gp

@router.post("/", response_model=GabinetePuertasOut)
def create_new_gabinete_puerta(data: GabinetePuertasCreate, db: Session = Depends(get_db)):
    return create_gabinete_puerta(db, data.dict())

@router.put("/{gabinete_id}/{puerta_id}", response_model=GabinetePuertasOut)
def update_existing_gabinete_puerta(gabinete_id: int, puerta_id: int, data: GabinetePuertasUpdate, db: Session = Depends(get_db)):
    return update_gabinete_puerta(db, gabinete_id, puerta_id, data.dict())

@router.delete("/{gabinete_id}/{puerta_id}")
def delete_existing_gabinete_puerta(gabinete_id: int, puerta_id: int, db: Session = Depends(get_db)):
    delete_gabinete_puerta(db, gabinete_id, puerta_id)
    return {"detail": "Deleted"}
