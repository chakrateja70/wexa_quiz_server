import re
from fastapi import HTTPException

def validate_password(password: str) -> bool:
    """
    Validates if the password meets the required criteria:
    - At least 8 characters long
    - At least one uppercase letter (A-Z)
    - At least one special character (!@#$%^&* etc.)
    - At least one digit (0-9)
    """
    if (
        len(password) < 8
        or not re.search(r"[A-Z]", password)  # At least one uppercase letter
        or not re.search(r"\W", password)  # At least one special character
        or not re.search(r"\d", password)  # At least one digit
    ):
        raise HTTPException(
            status_code=400,
            detail="Password must be at least 8 characters long, include one uppercase letter, one special character, and one digit."
        )
    return True
