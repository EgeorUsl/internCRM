from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from core.models import Branch
from .schemas import BranchSchema, BranchCreate


async def create_branch(session: AsyncSession,
                        branch_in: BranchCreate) -> Branch:
    branch = Branch(**branch_in.model_dump())
    session.add(branch)
    await session.commit()
    return branch


async def get_branches(session: AsyncSession) -> list[BranchSchema]:
    stmt = select(Branch).order_by(Branch.id)
    result: Result = await session.execute(stmt)
    branches = result.scalars().all()
    return list(branches)
