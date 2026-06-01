from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.database.models import User

from app.schemas.user_schema import (
    TokenResponse,
    UserResponse
)

from app.auth.security import (
    verify_password
)

from app.auth.jwt_handler import (
    create_access_token
)

from app.auth.dependencies import (
    get_current_user
)

from fastapi.security import OAuth2PasswordRequestForm



router = APIRouter()


@router.post(
    "/auth/login",
    response_model=TokenResponse
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    db_user = (
        db.query(User)
        .filter(
            User.username == form_data.username
        )
        .first()
    )

    if not db_user:

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    if not verify_password(
        form_data.password,
        db_user.hashed_password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    token = create_access_token(
        {
            "sub": db_user.username,
            "role": db_user.role
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.get(
    "/auth/me",
    response_model=UserResponse
)
def get_me(

    current_user: User = Depends(
        get_current_user
    )
):
    return current_user