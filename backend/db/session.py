from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.db.base import Base  # Opcional si no usás Base directamente aquí

DATABASE_URL = "postgresql://postgres:18452105@localhost:5432/Fleuba"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
