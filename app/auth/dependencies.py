from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.auth.jwt_handler import verify_token

from app.database.dependencies import get_db
from app.database.models import User


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/auth/login"
)


def get_current_user(

    token: str = Depends(
        oauth2_scheme
    ),

    db: Session = Depends(
        get_db
    )
):

    payload = verify_token(token)

    if not payload:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    username = payload.get("sub")

    user = (
        db.query(User)
        .filter(
            User.username == username
        )
        .first()
    )

    if not user:

        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    if not user.is_active:

        raise HTTPException(
            status_code=403,
            detail="User account disabled"
        )

    return user


def require_admin(

    current_user: User = Depends(
        get_current_user
    )
):

    if current_user.role != "ADMIN":

        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return current_user


def require_inventory_manager(

    current_user: User = Depends(
        get_current_user
    )
):

    allowed_roles = [
        "ADMIN",
        "INVENTORY_MANAGER"
    ]

    if current_user.role not in allowed_roles:

        raise HTTPException(
            status_code=403,
            detail="Inventory Manager access required"
        )

    return current_user


def require_data_scientist(

    current_user: User = Depends(
        get_current_user
    )
):

    allowed_roles = [
        "ADMIN",
        "DATA_SCIENTIST"
    ]

    if current_user.role not in allowed_roles:

        raise HTTPException(
            status_code=403,
            detail="Data Scientist access required"
        )

    return current_user


def require_ml_access(

    current_user: User = Depends(
        get_current_user
    )
):

    allowed_roles = [
        "ADMIN",
        "INVENTORY_MANAGER",
        "DATA_SCIENTIST"
    ]

    if current_user.role not in allowed_roles:

        raise HTTPException(
            status_code=403,
            detail="ML access required"
        )

    return current_user