from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from server.database.index import get_db
from server.database.models.question import Question, QuestionCreate, QuestionOut

class QuestionService:
    def get_all_questions(self, db: Session) -> list[QuestionOut]:
        """
        Retrieves all quiz questions from the database.
        """
        return db.query(Question).all()

    def create_question(self, db: Session, question: QuestionCreate) -> QuestionOut:
        """
        Creates a new quiz question in the database.
        """
        new_question = Question(
            question=question.question,
            option_a=question.option_a,
            option_b=question.option_b,
            option_c=question.option_c,
            option_d=question.option_d,
            correct_answer=question.correct_answer
        )
        db.add(new_question)
        db.commit()
        db.refresh(new_question)
        return new_question


class QuestionController:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
        self.question_service = QuestionService()

    def get_all_questions(self) -> list[QuestionOut]:
        """
        Retrieves all quiz questions.
        """
        questions = self.question_service.get_all_questions(self.db)
        if not questions:
            raise HTTPException(status_code=404, detail="No questions found.")
        return questions

    def create_question(self, question: QuestionCreate) -> QuestionOut:
        """
        Creates a new quiz question.
        """
        return self.question_service.create_question(self.db, question)
