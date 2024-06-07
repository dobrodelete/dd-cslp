from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, ConfigDict


class RoleBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    description: Optional[str] = None


class RoleCreate(RoleBase):
    pass


class RoleRead(RoleBase):
    id: int
    created_at: datetime

    # permissions: Optional[List["PermissionRead"]]
    # users: Optional[List["UserRead"]] = None


class RoleUpdate(RoleRead):
    pass
