from typing import Annotated
from annotated_types import MaxLen
from pydantic import BaseModel, ConfigDict


# class BranchCreate(BaseModel):
#     model_config = ConfigDict(from_attributes=True)
#
#     branch_name: Annotated[str, MaxLen(255)]


class StatusSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id:  int
    status_name: Annotated[str, MaxLen(255)]
