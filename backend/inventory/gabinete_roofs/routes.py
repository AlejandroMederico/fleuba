from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .service import get_gabinete_roofs, get_gabinete_roof, create_gabinete_roof, update_gabinete_roof, delete_gabinete_roof
from .schemas import GabineteRoofsCreate, GabineteRoofsUpdate, GabineteRoofsOut
from backend.db.session import get_db

router = APIRouter(prefix="/gabinete-roofs", tags=["GabineteRoofs"])

@router.get("/", response_model=list[GabineteRoofsOut])
def read_gabinete_roofs(db: Session = Depends(get_db)):
    return get_gabinete_roofs(db)

@router.get("/{gabinete_id}/{roof_id}", response_model=GabineteRoofsOut)
def read_gabinete_roof(gabinete_id: int, roof_id: int, db: Session = Depends(get_db)):
    gr = get_gabinete_roof(db, gabinete_id, roof_id)
    if not gr:
        raise HTTPException(status_code=404, detail="GabineteRoofs not found")
    return gr

@router.post("/", response_model=GabineteRoofsOut)
def create_new_gabinete_roof(data: GabineteRoofsCreate, db: Session = Depends(get_db)):
    return create_gabinete_roof(db, data.dict())

@router.put("/{gabinete_id}/{roof_id}", response_model=GabineteRoofsOut)
def update_existing_gabinete_roof(gabinete_id: int, roof_id: int, data: GabineteRoofsUpdate, db: Session = Depends(get_db)):
    return update_gabinete_roof(db, gabinete_id, roof_id, data.dict())

@router.delete("/{gabinete_id}/{roof_id}")
def delete_existing_gabinete_roof(gabinete_id: int, roof_id: int, db: Session = Depends(get_db)):
    delete_gabinete_roof(db, gabinete_id, roof_id)
    return {"detail": "Deleted"}
