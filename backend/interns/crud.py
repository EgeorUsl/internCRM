from pydantic.types import PositiveInt
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select
from sqlalchemy.engine import Result
from candidates.crud import get_candidates_by_city_and_by_cond
from core.models import Intern


async def get_interns_by_city_and_by_cond(session: AsyncSession,
                                          city_in: int,
                                          condition: str = "1=1"):
    stmt = select(Intern).where(
        Intern.city_id == city_in).where(text(condition)).order_by(Intern.group_id)
    result: Result = await session.execute(stmt)
    interns = result.scalars().all()
    return list(interns)


async def delete_interns_by_city(session: AsyncSession,
                                 city_id: PositiveInt):
    interns = await get_interns_by_city_and_by_cond(
        session=session, city_in=city_id)
    for intern in interns:
        await session.delete(intern)
    await session.commit()


async def convert_candidates_to_interns(session: AsyncSession,
                                        city_in: int,
                                        condition: str = "1=1"):

    candidates = await get_candidates_by_city_and_by_cond(
        session=session, city_in=city_in, condition=condition)

    for candidate in candidates:
        intern = Intern(
            first_name=candidate.first_name,
            last_name=candidate.last_name,
            email=candidate.email,
            studing_place=candidate.studing_place,
            education=candidate.education,
            status_id=candidate.status_id,
            city_id=candidate.city_id,
            branch_id=candidate.prefer_branch_id,
        )
        session.add(intern)
        await session.delete(candidate)
    await session.commit()
