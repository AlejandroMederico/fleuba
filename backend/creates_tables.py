from backend.db.base import Base
from backend.db.session import engine


def create_all_tables():
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas exitosamente")


if __name__ == "__main__":
    create_all_tables()
