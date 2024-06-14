from typing import Annotated
from annotated_types import MaxLen
from pydantic import BaseModel, ConfigDict


class CityCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    city_name: Annotated[str, MaxLen(255)]


class CitySchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id:  int
    city_name: Annotated[str, MaxLen(255)]
