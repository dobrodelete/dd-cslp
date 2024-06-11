from typing import Optional

from pydantic import BaseModel, ConfigDict
from datetime import datetime


class PasswordChangeBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    old_password_hash: bytes
    new_password_hash: bytes
    change_time: datetime


class PasswordChangeCreate(PasswordChangeBase):
    pass


class PasswordChangeRead(PasswordChangeBase):
    id: int
    created_at: datetime


class PasswordChangeUpdate(PasswordChangeRead):
    pass
