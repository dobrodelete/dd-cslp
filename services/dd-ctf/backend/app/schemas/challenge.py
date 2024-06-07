from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict


class ChallengeBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    title: str
    description: str
    category_id: int
    points: int
    flag: str


class ChallengeCreate(ChallengeBase):
    pass


class ChallengeRead(ChallengeBase):
    id: int
    created_at: datetime
    # hints: List["HintRead"] = []
    # submissions: List["SubmissionRead"] = []


class ChallengeUpdate(ChallengeRead):
    pass
