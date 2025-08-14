from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .service import get_gabinete_displays, get_gabinete_display, create_gabinete_display, update_gabinete_display, delete_gabinete_display
from .schemas import GabineteDisplaysCreate, GabineteDisplaysUpdate, GabineteDisplaysOut
from backend.db.session import get_db

router = APIRouter(prefix="/gabinete-displays", tags=["GabineteDisplays"])

@router.get("/", response_model=list[GabineteDisplaysOut])
def read_gabinete_displays(db: Session = Depends(get_db)):
    return get_gabinete_displays(db)

@router.get("/{gabinete_id}/{display_id}", response_model=GabineteDisplaysOut)
def read_gabinete_display(gabinete_id: int, display_id: int, db: Session = Depends(get_db)):
    gd = get_gabinete_display(db, gabinete_id, display_id)
    if not gd:
        raise HTTPException(status_code=404, detail="GabineteDisplays not found")
    return gd

@router.post("/", response_model=GabineteDisplaysOut)
def create_new_gabinete_display(data: GabineteDisplaysCreate, db: Session = Depends(get_db)):
    return create_gabinete_display(db, data.dict())

@router.put("/{gabinete_id}/{display_id}", response_model=GabineteDisplaysOut)
def update_existing_gabinete_display(gabinete_id: int, display_id: int, data: GabineteDisplaysUpdate, db: Session = Depends(get_db)):
    return update_gabinete_display(db, gabinete_id, display_id, data.dict())

@router.delete("/{gabinete_id}/{display_id}")
def delete_existing_gabinete_display(gabinete_id: int, display_id: int, db: Session = Depends(get_db)):
    delete_gabinete_display(db, gabinete_id, display_id)
    return {"detail": "Deleted"}
