from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .service import (
    get_puertas,
    get_puerta,
    create_puerta,
    update_puerta,
    delete_puerta,
)
from .schemas import PuertasCreate, PuertasUpdate, PuertasOut
from backend.db.session import get_db

router = APIRouter(prefix="/puertas", tags=["Puertas"])


@router.get("/", response_model=list[PuertasOut])
def read_puertas(db: Session = Depends(get_db)):
    return get_puertas(db)


@router.get("/{puerta_id}", response_model=PuertasOut)
def read_puerta(puerta_id: int, db: Session = Depends(get_db)):
    puerta = get_puerta(db, puerta_id)
    if not puerta:
        raise HTTPException(status_code=404, detail="Puerta not found")
    return puerta


@router.post("/", response_model=PuertasOut)
def create_new_puerta(puerta: PuertasCreate, db: Session = Depends(get_db)):
    return create_puerta(db, puerta.dict())


@router.put("/{puerta_id}", response_model=PuertasOut)
def update_existing_puerta(
    puerta_id: int, puerta: PuertasUpdate, db: Session = Depends(get_db)
):
    return update_puerta(db, puerta_id, puerta.dict())


@router.delete("/{puerta_id}")
def delete_existing_puerta(puerta_id: int, db: Session = Depends(get_db)):
    delete_puerta(db, puerta_id)
    return {"detail": "Deleted"}
