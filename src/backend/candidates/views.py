from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from . import crud
from .schemas import CandidateSchema, CreateCandidate
from core.auth.validation import (
    get_current_token_payload, get_current_active_auth_user)
from users.schemas import UserSchema

router = APIRouter(tags=["Candidates"])


@router.get("/candidates", response_model=list[CandidateSchema])
async def get_candidates(
    payload: dict = Depends(get_current_token_payload),
    user: UserSchema = Depends(get_current_active_auth_user),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_candidates(session=session)


@router.post("/create_candidate", response_model=CreateCandidate)
async def create_candidate(candidate_in: CreateCandidate,
                           session: AsyncSession = Depends(
                               db_helper.scoped_session_dependency),
                           ):
    return await crud.create_candidate(session=session,
                                       candidate_in=candidate_in)
