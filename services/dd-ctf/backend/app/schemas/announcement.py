from datetime import datetime

from pydantic import BaseModel, ConfigDict


class AnnouncementBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str
    content: str


class AnnouncementCreate(AnnouncementBase):
    pass


class AnnouncementRead(AnnouncementBase):
    id: int
    created_at: datetime
    updated_at: datetime


class AnnouncementUpdate(AnnouncementBase):
    id: int
