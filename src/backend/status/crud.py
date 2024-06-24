from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from core.models import Status
from .schemas import StatusSchema


# async def create_status(session: AsyncSession,
#                         branch_in: BranchCreate) -> Branch:
#     branch = Branch(**branch_in.model_dump())
#     session.add(branch)
#     await session.commit()
#     return branch


async def get_status(session: AsyncSession) -> list[StatusSchema]:
    stmt = select(Status).order_by(Status.id)
    result: Result = await session.execute(stmt)
    status = result.scalars().all()
    return list(status)
