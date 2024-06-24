from typing import Annotated, Optional
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, ConfigDict, EmailStr, PositiveInt


class CreateCandidate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    first_name: Annotated[str, MinLen(3), MaxLen(255)]
    last_name:  Annotated[str, MinLen(3), MaxLen(255)]
    email: EmailStr
    city_id: PositiveInt
    prefer_branch_id: PositiveInt
    studing_place: Annotated[str | None, MaxLen(255)] = None
    education: Annotated[str, MinLen(3), MaxLen(255)]
    target_internship: Optional[str | None] = None


class CandidateRead(BaseModel):
    id: int
    first_name: Annotated[str, MinLen(3), MaxLen(255)]
    last_name:  Annotated[str, MinLen(3), MaxLen(255)]
    email: EmailStr
    city: str
    status: str
    prefer_branch: str


class CandidateSchema(CreateCandidate):
    scores: int
    status_id: int
    status: str
    prefer_branch: str
    city: str
    completed_tests: int
