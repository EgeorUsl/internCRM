from typing import Annotated, Optional
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, ConfigDict, EmailStr


class CreateCandidate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    first_name: Annotated[str, MinLen(3), MaxLen(255)]
    last_name:  Annotated[str, MinLen(3), MaxLen(255)]
    email: EmailStr
    studing_place: Annotated[str, MaxLen(255)]
    education: Annotated[str, MinLen(3), MaxLen(255)]
    target_internship: Optional[str]
    city_id: int
    prefer_branch_id: int


class CandidateSchema(CreateCandidate):
    scores: int
    status: Optional[str]
    future_branch: Optional[str]
    completed_tests: int
