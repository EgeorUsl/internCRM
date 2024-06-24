from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper, User
from fastapi import HTTPException
from . import crud
from .schemas import CreateCandidate, CandidateRead
from core.auth.auth import current_superuser

router = APIRouter(tags=["Candidates"])


@router.delete("/delete_candidates_by_city/{city_id}")
async def delete_candidates_by_city(city_in: int,
                                    user: User = Depends(current_superuser),
                                    session: AsyncSession = Depends(
                                        db_helper.scoped_session_dependency)
                                    ):
    await crud.delete_candidates_by_city(session=session, city_in=city_in)


@router.get("/candidates/{candidate_id}", response_model=CandidateRead)
async def get_candidate_by_id(candidate_id: int,
                              user: User = Depends(current_superuser),
                              session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    try:
        candidate = await crud.get_candidate_by_id(session=session,
                                                   candidate_id=candidate_id)
    except HTTPException as e:
        raise e
    if not candidate:
        raise HTTPException(status_code=404, detail=f"Candidate with ID {
                            candidate_id} not found")
    return candidate


@router.get("/candidates")
async def get_candidates(user: User = Depends(current_superuser),
                         session: AsyncSession = Depends(
                             db_helper.scoped_session_dependency),
                         ):
    return await crud.get_candidates(session=session)


@router.get("/candidates-by-city/{city_in}")
async def get_candidates_by_city(city_in: int, user: User = Depends(current_superuser),
                                 session: AsyncSession = Depends(
                                     db_helper.scoped_session_dependency),
                                 ):
    return await crud.get_candidates_by_city(session=session, city_in=city_in)


@router.post("/create_candidate", response_model=CreateCandidate)
async def create_candidate(candidate_in: CreateCandidate,
                           session: AsyncSession = Depends(
                               db_helper.scoped_session_dependency),
                           ):
    try:
        candidate = await crud.create_candidate(session=session,
                                                candidate_in=candidate_in)
    except Exception:
        raise HTTPException(status_code=403, detail="Error creating candidate")
    return candidate

    # google_forms_link = await google_forms.get_google_forms_link(str(settings.google_forms.FORM_ID))
    # await email.send_email(candidate.email, email_body)
