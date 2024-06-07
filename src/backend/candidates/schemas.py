from typing import Annotated
from annotated_types import MinLen, MaxLen
from pydantic import BaseModel,  EmailStr


class CreateCandidate(BaseModel):
    first_name: Annotated[str, MinLen(3), MaxLen(255)]
    last_name:  Annotated[str, MinLen(3), MaxLen(255)]
    email: EmailStr
    studing_place: Annotated[str, MinLen(3), MaxLen(255)] = ""
    education: Annotated[str, MinLen(3), MaxLen(255)]
    target_internship: str = ""
    city: Annotated[str, MinLen(3), MaxLen(255)]
    prefer_branch: Annotated[str, MinLen(3), MaxLen(255)]
    resume: Annotated[str, MinLen(3), MaxLen(255)] = ""
