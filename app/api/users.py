from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.database.models import User

from app.schemas.user_schema import (
    UserCreate,
    UserUpdate,
    UserResponse
)

from app.auth.dependencies import (
    require_admin
)

from app.auth.security import (
    hash_password
)

from app.core.audit import (
    log_audit
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post(
    "/",
    response_model=UserResponse
)
def create_user(

    user: UserCreate,

    db: Session = Depends(get_db),

    current_user: User = Depends(
        require_admin
    )
):

    existing_user = (
        db.query(User)
        .filter(
            User.username == user.username
        )
        .first()
    )

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    db_user = User(

        username=user.username,

        email=user.email,

        hashed_password=hash_password(
            user.password
        ),

        role=user.role
    )

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    log_audit(
        db,
        current_user.username,
        "CREATE",
        "USER",
        f"Created user {user.username}"
    )

    return db_user

@router.get(
    "/",
    response_model=list[UserResponse]
)
def list_users(

    db: Session = Depends(get_db),

    current_user: User = Depends(
        require_admin
    )
):

    return db.query(User).all()

@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user(

    user_id: int,

    db: Session = Depends(get_db),

    current_user: User = Depends(
        require_admin
    )
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user

@router.put(
    "/{user_id}",
    response_model=UserResponse
)
def update_user(

    user_id: int,

    payload: UserUpdate,

    db: Session = Depends(get_db),

    current_user: User = Depends(
        require_admin
    )
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if payload.email is not None:
        user.email = payload.email

    if payload.role is not None:
        user.role = payload.role

    if payload.is_active is not None:
        user.is_active = payload.is_active

    db.commit()

    db.refresh(user)

    log_audit(
        db,
        current_user.username,
        "UPDATE",
        "USER",
        f"Updated user {user.username}"
    )

    return user

@router.patch("/{user_id}/disable")
def disable_user(

    user_id: int,

    db: Session = Depends(get_db),

    current_user: User = Depends(
        require_admin
    )
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.is_active = False

    db.commit()

    log_audit(
        db,
        current_user.username,
        "DISABLE",
        "USER",
        f"Disabled user {user.username}"
    )

    return {
        "message": "User disabled"
    }
    

@router.patch("/{user_id}/enable")
def enable_user(

    user_id: int,

    db: Session = Depends(get_db),

    current_user: User = Depends(
        require_admin
    )
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.is_active = True

    db.commit()

    log_audit(
        db,
        current_user.username,
        "ENABLE",
        "USER",
        f"Enabled user {user.username}"
    )

    return {
        "message": "User enabled"
    }

@router.delete("/{user_id}")
def delete_user(

    user_id: int,

    db: Session = Depends(get_db),

    current_user: User = Depends(
        require_admin
    )
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    username = user.username

    db.delete(user)

    db.commit()

    log_audit(
        db,
        current_user.username,
        "DELETE",
        "USER",
        f"Deleted user {username}"
    )

    return {
        "message": "User deleted"
    }