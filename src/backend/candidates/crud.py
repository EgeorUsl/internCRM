from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import CandidateSchema, CreateCandidate
from sqlalchemy import select
from sqlalchemy.engine import Result
from core.models import Candidate


async def create_candidate(session: AsyncSession,
                           candidate_in: CreateCandidate) -> Candidate:
    candidate = Candidate(**candidate_in.model_dump())
    session.add(candidate)
    await session.commit()
    return candidate


async def get_candidates(session: AsyncSession) -> list[CandidateSchema]:
    stmt = select(Candidate).order_by(Candidate.scores)
    result: Result = await session.execute(stmt)
    candidates = result.scalars().all()
    return list(candidates)
