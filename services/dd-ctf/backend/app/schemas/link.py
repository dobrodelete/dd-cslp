from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class LinkBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    url: str
    description: Optional[str] = None
    challenge_id: Optional[int] = None


class LinkCreate(LinkBase):
    pass


class LinkRead(LinkBase):
    id: int
    created_at: datetime


class LinkUpdate(LinkBase):
    id: int
