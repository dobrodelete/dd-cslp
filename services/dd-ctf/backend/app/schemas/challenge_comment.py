from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ChallengeCommentBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    challenge_id: int
    user_id: int
    content: str


class ChallengeCommentCreate(ChallengeCommentBase):
    pass


class ChallengeCommentRead(ChallengeCommentBase):
    id: int
    created_at: datetime
    updated_at: datetime


class ChallengeCommentUpdate(ChallengeCommentBase):
    id: int
