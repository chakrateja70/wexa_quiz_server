from sqlalchemy import Column, Integer, String
from server.database.index import Base
from pydantic import BaseModel, EmailStr

# SQLAlchemy User Model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

# Pydantic Schema for Creating User
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Pydantic Schema for User Login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Pydantic Schema for Output
class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
