
from typing import Annotated, Optional
from annotated_types import MaxLen, MinLen
from pydantic.main import BaseModel
from pydantic.networks import EmailStr
from pydantic.types import PositiveInt


class city_cond(BaseModel):
    city_in: int
    condition: str = "1=1"


class CreateIntern(BaseModel):
    first_name: Annotated[str, MinLen(3), MaxLen(255)]
    last_name:  Annotated[str, MinLen(3), MaxLen(255)]
    email: EmailStr
    city_id: PositiveInt
    branch_id: PositiveInt
    status_id: PositiveInt | None
    group_id: PositiveInt | None
    studing_place: Annotated[str | None, MaxLen(255)] = None
    education: Annotated[str, MinLen(3), MaxLen(255)]
    target_internship: Optional[str | None] = None
