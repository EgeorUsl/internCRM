from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from core.models import City
from .schemas import CitySchema, CityCreate


async def create_city(session: AsyncSession,
                      city_in: CityCreate) -> City:
    city = City(**city_in.model_dump())
    session.add(city)
    await session.commit()
    return city


async def get_cities(session: AsyncSession) -> list[CitySchema]:
    stmt = select(City).order_by(City.id)
    result: Result = await session.execute(stmt)
    cities = result.scalars().all()
    return list(cities)
