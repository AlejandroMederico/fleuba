from sqlalchemy.orm import Session
from typing import List, Optional
from . import models, schemas

def get_subcategory(db: Session, subcategory_id: int) -> Optional[models.Subcategory]:
    """Retrieve a subcategory by its ID."""
    return db.query(models.Subcategory).filter(
        models.Subcategory.id == subcategory_id,
        models.Subcategory.active == True
    ).first()

def get_subcategories(
    db: Session, 
    skip: int = 0, 
    limit: int = 100,
    category_id: Optional[int] = None
) -> List[models.Subcategory]:
    """Retrieve a list of subcategories, optionally filtered by category_id."""
    query = db.query(models.Subcategory).filter(models.Subcategory.active == True)
    if category_id is not None:
        query = query.filter(models.Subcategory.category_id == category_id)
    return query.offset(skip).limit(limit).all()

def create_subcategory(db: Session, subcategory: schemas.SubcategoryCreate) -> models.Subcategory:
    """Create a new subcategory."""
    db_subcategory = models.Subcategory(**subcategory.model_dump())
    db.add(db_subcategory)
    db.commit()
    db.refresh(db_subcategory)
    return db_subcategory

def update_subcategory(
    db: Session, 
    db_subcategory: models.Subcategory, 
    subcategory: schemas.SubcategoryUpdate
) -> models.Subcategory:
    """Update an existing subcategory."""
    update_data = subcategory.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_subcategory, field, value)
    db.add(db_subcategory)
    db.commit()
    db.refresh(db_subcategory)
    return db_subcategory

def delete_subcategory(db: Session, db_subcategory: models.Subcategory) -> models.Subcategory:
    """Perform a soft delete of a subcategory."""
    db_subcategory.active = False
    db.add(db_subcategory)
    db.commit()
    db.refresh(db_subcategory)
    return db_subcategory
