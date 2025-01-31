from fastapi import APIRouter, Depends
from server.controllers.auth import AuthController
from server.database.models.index import UserLogin

router = APIRouter(prefix="/auth/login", tags=["Authentication"])

@router.post("/")
def login(user: UserLogin, controller: AuthController = Depends()):
    """
    Logs in a user and returns a JWT access token.
    """
    return controller.login_user(user)