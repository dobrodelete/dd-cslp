from pydantic import BaseModel, ConfigDict


class HintBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    challenge_id: int
    content: str
    cost: int


class HintCreate(HintBase):
    pass


class HintRead(HintBase):
    id: int


class HintUpdate(HintRead):
    pass
