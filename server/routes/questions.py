from fastapi import APIRouter, Depends
from server.controllers.question import QuestionController
from server.database.models import QuestionCreate, QuestionOut
from server.services.auth import get_current_user

router = APIRouter(prefix="/questions", tags=["Quiz Questions"])

@router.get("/", response_model=list[QuestionOut])
def get_questions(controller: QuestionController = Depends()):
    """
    Retrieves all quiz questions.
    """
    return controller.get_all_questions()

@router.post("/", response_model=QuestionOut)
def create_question(
    question: QuestionCreate,
    controller: QuestionController = Depends(),
    user: str = Depends(get_current_user),  # Validate token and get the user
):
    """
    Creates a new quiz question (Authenticated).
    """
    return controller.create_question(question)
