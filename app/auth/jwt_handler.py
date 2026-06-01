from datetime import datetime
from datetime import timedelta
from datetime import UTC

from jose import jwt
from jose import JWTError

from app.config import (
    JWT_SECRET_KEY,
    JWT_ALGORITHM,
    JWT_EXPIRE_MINUTES
)


def create_access_token(data: dict):

    payload = data.copy()

    expire = (
        datetime.now(UTC)
        + timedelta(
            minutes=JWT_EXPIRE_MINUTES
        )
    )

    payload.update(
        {
            "exp": expire
        }
    )

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM
    )


def verify_token(token: str):

    try:

        payload = jwt.decode(
            token,
            JWT_SECRET_KEY,
            algorithms=[
                JWT_ALGORITHM
            ]
        )

        return payload

    except JWTError:

        return None