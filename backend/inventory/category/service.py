from sqlalchemy.orm import Session
from .models import Category
from .schemas import CategoryCreate, CategoryBase


def get_all_categories(db: Session):
    return db.query(Category).filter(Category.active == True).all()


def get_category(db: Session, category_id: int):
    return (
        db.query(Category)
        .filter(Category.id == category_id, Category.active == True)
        .first()
    )


def create_category(db: Session, category_in: CategoryCreate):
    category = Category(**category_in.model_dump())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def update_category(db: Session, category_id: int, category_in: CategoryBase):
    category = (
        db.query(Category)
        .filter(Category.id == category_id, Category.active == True)
        .first()
    )
    if not category:
        return None
    for field, value in category_in.model_dump(exclude_unset=True).items():
        setattr(category, field, value)
    db.commit()
    db.refresh(category)
    return category


def delete_category(db: Session, category_id: int):
    category = (
        db.query(Category)
        .filter(Category.id == category_id, Category.active == True)
        .first()
    )
    if not category:
        return None
    category.active = False
    db.commit()
    db.refresh(category)
    return category
