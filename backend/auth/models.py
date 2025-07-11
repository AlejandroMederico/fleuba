from sqlalchemy import Column, Integer, String
from backend.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="user")
    auth_provider = Column(String, default="local")  # 👈 este campo es clave
    firebase_uid = Column(String, unique=True, nullable=True)
