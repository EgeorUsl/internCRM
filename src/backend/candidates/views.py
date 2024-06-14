from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from . import crud
from .schemas import CandidateSchema, CreateCandidate
from config import settings
# from core.tests_forms import google_forms

router = APIRouter(tags=["Candidates"])


@router.get("/candidates", response_model=list[CandidateSchema])
async def get_candidates(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_candidates(session=session)


@router.post("/create_candidate", response_model=CreateCandidate)
async def create_candidate(candidate_in: CreateCandidate,
                           session: AsyncSession = Depends(
                               db_helper.scoped_session_dependency),
                           ):
    candidate = await crud.create_candidate(session=session,
                                            candidate_in=candidate_in)
    return candidate

    # google_forms_link = await google_forms.get_google_forms_link(str(settings.google_forms.FORM_ID))
    # await email.send_email(candidate.email, email_body)
