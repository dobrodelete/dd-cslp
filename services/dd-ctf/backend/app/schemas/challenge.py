from datetime import datetime
from typing import List, Optional

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
    updated_at: datetime


class ChallengeUpdate(ChallengeRead):
    pass


class Challenges(BaseModel):
    challenges: Optional[ChallengeRead]
    total: Optional[int]
