from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from . import crud
from .schemas import CitySchema, CityCreate

router = APIRouter(tags=["Cities"])


@router.get("/cities", response_model=list[CitySchema])
async def get_cities(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_cities(session=session)


@router.post("/create_city", response_model=CityCreate)
async def create_city(city_in: CityCreate,
                      session: AsyncSession = Depends(
                          db_helper.scoped_session_dependency),
                      ):
    cities = await crud.create_city(session=session,
                                    city_in=city_in)
    return cities
