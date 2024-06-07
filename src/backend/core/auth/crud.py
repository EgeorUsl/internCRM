from core.auth import utils as auth_utils
from typing import Sequence
from users.schemas import UserSchema
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from sqlalchemy.engine import Result
from core.models import db_helper
from sqlalchemy import select, text
from core.models import User
import asyncio


async def Users_in_db(session: AsyncSession):
    query = text("SELECT username, password FROM users")
    res: Result = await session.execute(query)
    rows = res.scalars().all()
    user_dict = {}
    for row in rows:
        user = UserSchema(username=row.username,
                          password=bytes(row.password, 'utf-8'))
        user_dict[row.username] = user
    return user_dict

sam = UserSchema(
    username="sam",
    password=auth_utils.hash_password("secret"),
)

users_db: dict[str, UserSchema] = {sam.username: sam
                                   }
# users_db: dict[str, UserSchema] = asyncio.run(Users_in_db(
#     Depends(db_helper.scoped_session_dependency)))
