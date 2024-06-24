from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from . import crud
from .schemas import BranchSchema, BranchCreate

router = APIRouter(tags=["Branches"])


@router.get("/branches",)
async def get_branches(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_branches(session=session)


@router.get("/branches/groups",)
async def get_groups(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_groups(session=session)


@router.get("/branches_with_groups",)
async def get_branches_with_groups(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_branches_with_groups(session=session)

# @router.post("/create_branch", response_model=BranchCreate)
# async def create_branch(branch_in: BranchCreate,
#                         session: AsyncSession = Depends(
#                             db_helper.scoped_session_dependency),
#                         ):
#     branches = await crud.create_branch(session=session,
#                                         branch_in=branch_in)
#     return branches
