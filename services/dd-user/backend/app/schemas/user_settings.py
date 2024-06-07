from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class UserSettingsBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    setting_name: str
    setting_value: str
    last_updated: datetime


class UserSettingsCreate(UserSettingsBase):
    pass


class UserSettingsRead(UserSettingsBase):
    id: int
    created_at: datetime

    # user: Optional["UserRead"] = None


class UserSettingsUpdate(UserSettingsRead):
    pass
