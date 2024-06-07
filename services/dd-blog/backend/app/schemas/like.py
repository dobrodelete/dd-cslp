from datetime import datetime

from pydantic import BaseModel, ConfigDict


class LikeBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    post_id: int
    user_id: int


class LikeCreate(LikeBase):
    pass


class LikeRead(LikeBase):
    id: int
    created_at: datetime


class LikeUpdate(LikeRead):
    pass
