from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, EmailStr, ConfigDict, Field


class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    username: str
    email: EmailStr
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    is_admin: bool = False
    is_active: bool = True


class UserCreate(UserBase):
    password: str
    password_hash: Optional[bytes] = None


class UserRead(UserBase):
    id: int
    password_hash: bytes
    created_at: datetime
    updated_at: datetime

    # roles: Optional[List["RoleRead"]] = Field(default=None)
    # permissions: Optional[List["PermissionRead"]] = Field(default=None)
    # login_attempts: Optional[List["LoginAttemptRead"]] = Field(default=None)
    # password_changes: Optional[List["PasswordChangeRead"]] = Field(default=None)
    # user_access_log: Optional[List["UserAccessLogRead"]] = Field(default=None)
    # user_security: Optional[List["UserSecurityRead"]] = Field(default=None)
    # user_session: Optional[List["UserSessionRead"]] = Field(default=None)
    # user_settings: Optional[List["UserSettingsRead"]] = Field(default=None)


class UserSchema(UserBase):
    id: int
    # password_hash: bytes
    created_at: datetime
    updated_at: datetime


class UserUpdate(UserRead):
    active: Optional[bool] = None
