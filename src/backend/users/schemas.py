
from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, ConfigDict


class CreateUser(BaseModel):
    model_config = ConfigDict(strict=True)
    username: Annotated[str, MinLen(3), MaxLen(255)]
    password: bytes


class UserSchema(BaseModel):
    model_config = ConfigDict(strict=True)

    username: Annotated[str, MinLen(3), MaxLen(255)]
    password: bytes
    active: bool = True
