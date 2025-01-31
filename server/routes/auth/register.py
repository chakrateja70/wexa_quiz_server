


from fastapi import APIRouter, Depends
from server.controllers.auth import AuthController
from server.database.models.index import UserCreate, UserOut

router = APIRouter(prefix="/auth/register", tags=["Authentication"])

@router.post("/", response_model=UserOut)
def register(user: UserCreate, controller: AuthController = Depends()):
    """
    Registers a new user.
    """
    return controller.register_user(user)
