from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, text, func, join
from sqlalchemy.orm import joinedload
from sqlalchemy.engine import Result
from core.models import Branch, Group
from .schemas import BranchSchema, BranchCreate


async def create_branch(session: AsyncSession,
                        branch_in: BranchCreate) -> Branch:
    branch = Branch(**branch_in.model_dump())
    session.add(branch)
    await session.commit()
    return branch


async def get_branches_with_groups(session: AsyncSession):
    stmt = (
        select(
            Branch.id,
            Branch.branch_name,
            func.group_concat(Group.group_name).label("groups")
        )
        .select_from(join(Branch, Group, Branch.id == Group.branch_id))
        .group_by(Branch.branch_name)
        .order_by(Branch.branch_name)
    )
    result: Result = await session.execute(stmt)
    branches = result.all()
    list_of_dicts = []
    for id, branch_name, groups in branches:
        groups_list = groups.split(',')
        list_of_dicts.append(
            {'id': id, 'branch_name': branch_name, 'groups': groups_list})
    return list_of_dicts


async def get_branches(session: AsyncSession):
    stmt = select(Branch).order_by(Branch.id)
    result: Result = await session.execute(stmt)
    branches = result.scalars().all()
    return list(branches)


async def get_groups(session: AsyncSession):
    stmt = select(Group).order_by(Group.id)
    result: Result = await session.execute(stmt)
    groups = result.scalars().all()
    return list(groups)
