from fastapi import APIRouter, Depends
from pydantic.types import PositiveInt
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper, User
from fastapi import HTTPException
from . import crud
from core.auth.auth import current_superuser
from .schemas import city_cond

router = APIRouter(tags=["Interns"])


@router.delete("/delete_interns_by_city/{city_id}")
async def delete_interns_by_city(city_id: int,
                                 user: User = Depends(current_superuser),
                                 session: AsyncSession = Depends(
                                     db_helper.scoped_session_dependency)
                                 ):
    await crud.delete_interns_by_city(session=session, city_id=city_id)


@router.post("/create_interns")
async def convert_candidates_to_interns(city_c: city_cond,
                                        user: User = Depends(
                                            current_superuser),
                                        session: AsyncSession =
                                        Depends(db_helper.scoped_session_dependency)):
    await crud.convert_candidates_to_interns(session=session,
                                             city_in=city_c.city_in,
                                             condition=city_c.condition)


@router.get("/interns-by-city/{city_in}")
async def get_interns_by_city(city_in: PositiveInt,
                              user: User = Depends(current_superuser),
                              session: AsyncSession = Depends(
                                  db_helper.scoped_session_dependency),
                              ):
    return await crud.get_interns_by_city_and_by_cond(session=session,
                                                      city_in=city_in,
                                                      condition="1=1")
