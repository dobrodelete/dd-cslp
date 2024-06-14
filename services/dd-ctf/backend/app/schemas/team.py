from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class TeamBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    description: Optional[str] = None


class TeamCreate(TeamBase):
    pass


class TeamRead(TeamBase):
    id: int
    created_at: datetime


class TeamUpdate(TeamRead):
    id: int
