from typing import Optional

from pydantic import BaseModel, ConfigDict, IPvAnyAddress
from datetime import datetime


class LoginAttemptBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    user_id: int
    attempt_time: datetime
    ip_address_v4: IPvAnyAddress
    ip_address_v6: Optional[IPvAnyAddress] = None
    user_agent: str
    successful: bool


class LoginAttemptCreate(LoginAttemptBase):
    pass


class LoginAttemptRead(LoginAttemptBase):
    id: int
    created_at: datetime

    # user: Optional["UserRead"] = None


class LoginAttemptUpdate(LoginAttemptRead):
    pass
