from typing import Optional

from pydantic import BaseModel, ConfigDict
from datetime import datetime


class UserSessionBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id: int
    session_token: str
    expires_at: datetime
    ip_address: str
    user_agent: str


class UserSessionCreate(UserSessionBase):
    pass


class UserSessionRead(UserSessionBase):
    id: int

    # user: Optional["UserRead"] = None


class UserSessionUpdate(UserSessionRead):
    pass
