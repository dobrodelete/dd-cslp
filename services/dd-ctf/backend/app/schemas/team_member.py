from pydantic import BaseModel, ConfigDict
from datetime import datetime


class TeamMemberBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    team_id: int
    user_id: int


class TeamMemberCreate(TeamMemberBase):
    pass


class TeamMemberRead(TeamMemberBase):
    id: int
    joined_at: datetime
    created_at: datetime
    updated_at: datetime


class TeamMemberUpdate(TeamMemberRead):
    id: int
