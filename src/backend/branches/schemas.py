from typing import Annotated
from annotated_types import MaxLen
from pydantic import BaseModel, ConfigDict


class BranchCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    branch_name: Annotated[str, MaxLen(255)]
    groups_list: list


class BranchSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id:  int
    branch_name: Annotated[str, MaxLen(255)]
    # groups_list: list
