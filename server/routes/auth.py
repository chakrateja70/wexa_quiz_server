from fastapi import APIRouter, Depends
from server.controllers.auth import AuthController
from server.database.models import UserCreate, UserLogin, UserOut

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, controller: AuthController = Depends()):
    """
    Registers a new user.
    """
    return controller.register_user(user)

@router.post("/login")
def login(user: UserLogin, controller: AuthController = Depends()):
    """
    Logs in a user and returns a JWT access token.
    """
    return controller.login_user(user)
