from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from app.enums import AccessStatus


class UserAccessLogBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    timestamp: datetime
    ip_address: str
    action: str
    status: AccessStatus
    user_agent: str
    location: Optional[str] = None


class UserAccessLogCreate(UserAccessLogBase):
    pass


class UserAccessLogRead(UserAccessLogBase):
    id: int
    created_at: datetime


class UserAccessLogUpdate(UserAccessLogRead):
    pass
