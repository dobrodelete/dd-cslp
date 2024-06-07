from typing import Optional

from pydantic import BaseModel, ConfigDict, IPvAnyAddress
from datetime import datetime


class BlockedIPBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    block: bool = True
    ip_address_v4: IPvAnyAddress
    ip_address_v6: Optional[IPvAnyAddress]
    block_reason: str


class BlockedIPCreate(BlockedIPBase):
    pass


class BlockedIPRead(BlockedIPBase):
    id: int
    created_at: datetime
    blocked_at: datetime


class BlockedIPUpdate(BlockedIPRead):
    pass
