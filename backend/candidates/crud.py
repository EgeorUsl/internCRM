from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import CandidateSchema, CreateCandidate
from sqlalchemy import select, delete, text
from sqlalchemy.engine import Result
from core.models import Candidate


async def delete_candidates_by_city(city_in: int, session: AsyncSession
                                    ):
    # stmt = delete(Candidate).filter(Candidate.city_id == city_in)
    stmt = text(f'DELETE FROM `candidates` WHERE `city_id` = {city_in}')
    await session.execute(stmt)


async def create_candidate(session: AsyncSession,
                           candidate_in: CreateCandidate) -> Candidate:
    candidate = Candidate(**candidate_in.model_dump())
    session.add(candidate)
    await session.commit()
    return candidate


async def get_candidates_by_city(session: AsyncSession, city_in: int):
    stmt = select(Candidate).order_by(
        Candidate.id).where(Candidate.city_id == city_in)
    result: Result = await session.execute(stmt)
    candidates = result.scalars().all()
    return list(candidates)


async def get_candidates_by_city_and_by_cond(session: AsyncSession,
                                             city_in: int,
                                             condition: str = "1=1"):
    stmt = select(Candidate).where(
        Candidate.city_id == city_in).where(text(condition))
    result: Result = await session.execute(stmt)
    candidates = result.scalars().all()
    return list(candidates)


async def get_candidates(session: AsyncSession):
    stmt = select(Candidate).order_by(
        Candidate.id)
    result: Result = await session.execute(stmt)
    candidates = result.scalars().all()
    return list(candidates)


async def get_candidate_by_id(session: AsyncSession, candidate_id: int):
    stmt = select(Candidate).where(Candidate.id == candidate_id)
    result: Result = await session.execute(stmt)
    candidate = result.scalar_one_or_none()
    return candidate
