from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Candidate

from .schemas import CandidateCreate


# async def create_candidate(session: AsyncSession, candidate_in: ProductCreate) -> Candidate:
#     candidate = Product(**product_in.model_dump())
#     session.add(product)
#     await session.commit()
#     # await session.refresh(product)
#     return product
