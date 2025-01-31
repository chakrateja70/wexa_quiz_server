from fastapi import APIRouter, Depends
from server.controllers.auth.login import LoginController
from server.database.models.user import UserLogin

router = APIRouter(prefix="/auth/login", tags=["Authentication"])

@router.post("/")
def login(user: UserLogin, controller: LoginController = Depends()):
    """
    Logs in a user and returns a JWT access token.
    """
    return controller.login_user(user)
