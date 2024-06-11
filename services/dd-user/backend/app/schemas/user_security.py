from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class UserSecurityBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    last_login: datetime
    login_attempts: int
    last_failed_login: Optional[datetime] = None
    password_changed_at: Optional[datetime] = None
    password_reset_token: Optional[str] = None
    password_reset_token_expires_at: Optional[datetime] = None
    account_lock: bool = False
    account_lock_until: Optional[datetime] = None


class UserSecurityCreate(UserSecurityBase):
    pass


class UserSecurityRead(UserSecurityBase):
    id: int
    created_at: datetime


class UserSecurityUpdate(UserSecurityRead):
    pass
