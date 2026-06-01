from pydantic import BaseModel
from pydantic import ConfigDict
from typing import Optional


class UserCreate(BaseModel):

    username: str

    email: str

    password: str

    role: Optional[str] = "VIEWER"


class UserLogin(BaseModel):

    username: str

    password: str


class UserResponse(BaseModel):

    id: int

    username: str

    email: str

    role: str

    is_active: bool

    model_config = ConfigDict(
        from_attributes=True
    )

class UserUpdate(BaseModel):

    email: Optional[str] = None

    role: Optional[str] = None

    is_active: Optional[bool] = None


class UserStatusResponse(BaseModel):

    message: str

class TokenResponse(BaseModel):

    access_token: str

    token_type: str