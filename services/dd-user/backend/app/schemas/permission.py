from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, ConfigDict


class PermissionBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    description: Optional[str] = None


class PermissionCreate(PermissionBase):
    pass


class PermissionRead(PermissionBase):
    id: int
    created_at: datetime


class PermissionUpdate(PermissionRead):
    pass


class PermissionRoleRead(PermissionRead):
    roles: Optional[List["RoleRead"]] = None
