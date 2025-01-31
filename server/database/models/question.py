from sqlalchemy import Column, Integer, String
from server.database.index import Base
from pydantic import BaseModel

# SQLAlchemy Question Model
class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    option_a = Column(String, nullable=False)
    option_b = Column(String, nullable=False)
    option_c = Column(String, nullable=False)
    option_d = Column(String, nullable=False)
    correct_answer = Column(Integer, nullable=False)

# Pydantic Schema for Creating Question
class QuestionCreate(BaseModel):
    question: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: int

# Pydantic Schema for Output
class QuestionOut(BaseModel):
    id: int
    question: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_answer: int

    class Config:
        orm_mode = True
