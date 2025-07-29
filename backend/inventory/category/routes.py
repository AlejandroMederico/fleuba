from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import service, schemas
from backend.db.session import get_db  # Asegúrate de tener este método

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("/", response_model=list[schemas.Category])
def list_categories(db: Session = Depends(get_db)):
    return service.get_all_categories(db)


@router.post("/", response_model=schemas.Category)
def add_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return service.create_category(db, category)
