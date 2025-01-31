from sqlalchemy.orm import Session
from server.database.models import Question
from server.database.models import QuestionCreate, QuestionOut

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
