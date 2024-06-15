from datetime import datetime
from typing import Optional

from pydantic import ConfigDict, BaseModel


class CTFEventBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime
    active: bool


class CTFEventCreate(CTFEventBase):
    pass


class CTFEventRead(CTFEventBase):
    id: int
    created_at: datetime


class CTFEventUpdate(CTFEventBase):
    id: int
