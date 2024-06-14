from pydantic import BaseModel, ConfigDict
from datetime import datetime


class HintBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    challenge_id: int
    content: str
    cost: int


class HintCreate(HintBase):
    pass


class HintRead(HintBase):
    id: int
    created_at: datetime


class HintUpdate(HintRead):
    id: int
