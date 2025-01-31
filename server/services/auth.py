from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from server.utils.auth import validate_password
from server.database.config.index import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

# OAuth2 scheme to extract token from the Authorization header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


class AuthService:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(self, password: str) -> str:
        """
        Hashes the user's password using bcrypt.
        """
        validate_password(password)  # Ensure password meets security requirements
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """
        Verifies if the given plain password matches the stored hashed password.
        """
        return self.pwd_context.verify(plain_password, hashed_password)

    def create_access_token(self, data: dict) -> str:
        """
        Creates a JWT access token.
        """
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
    def verify_access_token(self, token: str) -> dict:
        """
        Verifies the JWT access token and decodes its payload.
        """
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except JWTError:
            raise HTTPException(
                status_code=401,
                detail="Invalid or expired token",
            )


# Dependency to extract and validate current user from the token
def get_current_user(token: str = Depends(oauth2_scheme), auth_service: AuthService = Depends()) -> dict:
    """
    Extracts and validates the current user from the JWT token.
    """
    payload = auth_service.verify_access_token(token)
    if "sub" not in payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token: subject claim is missing",
        )
    return payload["sub"]  # Typically the user's email or ID
