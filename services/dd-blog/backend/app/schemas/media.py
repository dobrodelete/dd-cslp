from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class MediaBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    url: str
    post_id: Optional[int] = None
    page_id: Optional[int] = None


class MediaCreate(MediaBase):
    pass


class MediaRead(MediaBase):
    id: int
    uploaded_at: datetime


class MediaUpdate(MediaRead):
    pass
