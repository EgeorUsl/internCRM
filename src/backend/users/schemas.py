
from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, ConfigDict, EmailStr
from fastapi_users import schemas
from typing import Optional


class RoleSchema(BaseModel):
    name: str
    permissions: dict


class UserRead(schemas.BaseUser[int]):
    model_config = ConfigDict(from_attributes=True)

    email: EmailStr
    username: str
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: EmailStr
    password: str
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
