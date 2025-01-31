from fastapi import APIRouter, Depends
from server.controllers.auth.register import RegisterController
from server.database.models.user import UserCreate, UserOut

router = APIRouter(prefix="/auth/register", tags=["Authentication"])

@router.post("/", response_model=UserOut)
def register(user: UserCreate, controller: RegisterController = Depends()):
    """
    Registers a new user.
    """
    return controller.register_user(user)
