from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from server.database.index import get_db
from server.database.models.user import User
from server.database.models.user import UserCreate, UserOut
from server.services.auth import AuthService

class RegisterController:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
        self.auth_service = AuthService()

    def register_user(self, user: UserCreate) -> UserOut:
        """
        Registers a new user by hashing their password and storing the credentials.
        """
        existing_user = self.db.query(User).filter(User.email == user.email).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
            )

        hashed_password = self.auth_service.hash_password(user.password)
        new_user = User(
            username=user.username, email=user.email, hashed_password=hashed_password
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
