from .schemas import RoleSchema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from core.models import User, Role


async def create_role(session: AsyncSession,
                      role_in: RoleSchema) -> Role:
    role = Role(**role_in.model_dump())
    session.add(role)
    await session.commit()
    return role
