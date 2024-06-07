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

    # roles: Optional[List["RoleRead"]] = None
    # users: Optional[List["UserRead"]] = None


class PermissionUpdate(PermissionRead):
    pass
