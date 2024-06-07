from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SubmissionBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    challenge_id: int
    user_id: int
    flag: str
    correct: bool


class SubmissionCreate(SubmissionBase):
    pass


class SubmissionRead(SubmissionBase):
    id: int
    submission_time: datetime


class SubmissionUpdate(SubmissionRead):
    pass
