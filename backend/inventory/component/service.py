from .models import Component
from sqlalchemy.orm import Session

def get_components(db: Session):
    return db.query(Component).all()

def get_component(db: Session, component_id: int):
    return db.query(Component).filter(Component.id == component_id).first()

def create_component(db: Session, component_data):
    component = Component(**component_data)
    db.add(component)
    db.commit()
    db.refresh(component)
    return component

def update_component(db: Session, component_id: int, component_data):
    component = get_component(db, component_id)
    for key, value in component_data.items():
        setattr(component, key, value)
    db.commit()
    db.refresh(component)
    return component

def delete_component(db: Session, component_id: int):
    component = get_component(db, component_id)
    db.delete(component)
    db.commit()
