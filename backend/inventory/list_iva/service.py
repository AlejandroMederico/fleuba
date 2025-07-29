from sqlalchemy.orm import Session
from typing import List, Optional
from . import models, schemas

def get_iva(db: Session, iva_id: int) -> Optional[models.ListIva]:
    """Retrieve an IVA rate by its ID."""
    return db.query(models.ListIva).filter(
        models.ListIva.id == iva_id,
        models.ListIva.active == True
    ).first()

def get_all_ivas(
    db: Session, 
    skip: int = 0, 
    limit: int = 100,
    active_only: bool = True
) -> List[models.ListIva]:
    """Retrieve a list of IVA rates, optionally filtered by active status."""
    query = db.query(models.ListIva)
    if active_only:
        query = query.filter(models.ListIva.active == True)
    return query.offset(skip).limit(limit).all()

def create_iva(db: Session, iva: schemas.ListIvaCreate) -> models.ListIva:
    """Create a new IVA rate."""
    db_iva = models.ListIva(**iva.model_dump())
    db.add(db_iva)
    db.commit()
    db.refresh(db_iva)
    return db_iva

def update_iva(
    db: Session, 
    db_iva: models.ListIva, 
    iva: schemas.ListIvaUpdate
) -> models.ListIva:
    """Update an existing IVA rate."""
    update_data = iva.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_iva, field, value)
    db.add(db_iva)
    db.commit()
    db.refresh(db_iva)
    return db_iva

def delete_iva(db: Session, db_iva: models.ListIva) -> models.ListIva:
    """Perform a soft delete of an IVA rate."""
    db_iva.active = False
    db.add(db_iva)
    db.commit()
    db.refresh(db_iva)
    return db_iva
