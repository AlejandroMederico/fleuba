from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .service import get_gabinete_cartridges, get_gabinete_cartridge, create_gabinete_cartridge, update_gabinete_cartridge, delete_gabinete_cartridge
from .schemas import GabineteCartridgesCreate, GabineteCartridgesUpdate, GabineteCartridgesOut
from backend.db.session import get_db

router = APIRouter(prefix="/gabinete-cartridges", tags=["GabineteCartridges"])

@router.get("/", response_model=list[GabineteCartridgesOut])
def read_gabinete_cartridges(db: Session = Depends(get_db)):
    return get_gabinete_cartridges(db)

@router.get("/{gabinete_id}/{cartridge_id}", response_model=GabineteCartridgesOut)
def read_gabinete_cartridge(gabinete_id: int, cartridge_id: int, db: Session = Depends(get_db)):
    gc = get_gabinete_cartridge(db, gabinete_id, cartridge_id)
    if not gc:
        raise HTTPException(status_code=404, detail="GabineteCartridges not found")
    return gc

@router.post("/", response_model=GabineteCartridgesOut)
def create_new_gabinete_cartridge(data: GabineteCartridgesCreate, db: Session = Depends(get_db)):
    return create_gabinete_cartridge(db, data.dict())

@router.put("/{gabinete_id}/{cartridge_id}", response_model=GabineteCartridgesOut)
def update_existing_gabinete_cartridge(gabinete_id: int, cartridge_id: int, data: GabineteCartridgesUpdate, db: Session = Depends(get_db)):
    return update_gabinete_cartridge(db, gabinete_id, cartridge_id, data.dict())

@router.delete("/{gabinete_id}/{cartridge_id}")
def delete_existing_gabinete_cartridge(gabinete_id: int, cartridge_id: int, db: Session = Depends(get_db)):
    delete_gabinete_cartridge(db, gabinete_id, cartridge_id)
    return {"detail": "Deleted"}
