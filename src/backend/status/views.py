from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from . import crud
from .schemas import BranchSchema, BranchCreate

router = APIRouter(tags=["Branches"])


@router.get("/branches", response_model=list[BranchSchema])
async def get_branches(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_branches(session=session)


@router.post("/create_branch", response_model=BranchCreate)
async def create_branch(branch_in: BranchCreate,
                        session: AsyncSession = Depends(
                            db_helper.scoped_session_dependency),
                        ):
    branches = await crud.create_branch(session=session,
                                        branch_in=branch_in)
    return branches
