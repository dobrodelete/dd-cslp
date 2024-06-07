from pydantic import BaseModel, ConfigDict
from typing import Optional


class TagBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    description: Optional[str] = None


class TagCreate(TagBase):
    pass


class TagRead(TagBase):
    id: int


class TagUpdate(TagRead):
    pass
