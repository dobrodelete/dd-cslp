from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ChallengeRatingBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    challenge_id: int
    user_id: int
    rating: int


class ChallengeRatingCreate(ChallengeRatingBase):
    pass


class ChallengeRatingRead(ChallengeRatingBase):
    id: int
    created_at: datetime
    updated_at: datetime


class ChallengeRatingUpdate(ChallengeRatingBase):
    id: int
