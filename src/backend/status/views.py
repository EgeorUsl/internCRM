from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from .schemas import StatusSchema
from . import crud

router = APIRouter(tags=["Status"])


@router.get("/status", response_model=list[StatusSchema])
async def get_status(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_status(session=session)


# @router.post("/create_branch", response_model=BranchCreate)
# async def create_branch(branch_in: BranchCreate,
#                         session: AsyncSession = Depends(
#                             db_helper.scoped_session_dependency),
#                         ):
#     branches = await crud.create_branch(session=session,
#                                         branch_in=branch_in)
#     return branches
