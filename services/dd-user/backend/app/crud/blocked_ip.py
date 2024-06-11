from typing import Optional, List

from sqlalchemy import select, update, delete, insert, func

from app.crud import CrudBase
from app.models import BlockedIPs
from app.schemas import BlockedIPCreate, BlockedIPUpdate, BlockedIPRead


class BlockedIPCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_blocked_ip(self, id: int) -> Optional[BlockedIPRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(BlockedIPs).where(BlockedIPs.id == id))
            blocked_ip: Optional[BlockedIPs] = result.scalar()
            return BlockedIPRead.model_validate(blocked_ip) if blocked_ip else None

    async def get_blocked_ips(self, skip: int = 0, limit: int = 999) -> Optional[List[BlockedIPRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(BlockedIPs).offset(skip).limit(limit))
            blocked_ips: Optional[List[BlockedIPs]] = result.scalars().all()
            return [BlockedIPRead.model_validate(blocked_ip) for blocked_ip in blocked_ips] if blocked_ips else None

    async def get_blocked_ip_by_v4(self, ip_address_v4: str) -> Optional[BlockedIPRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(BlockedIPs).where(BlockedIPs.ip_address_v4 == ip_address_v4))
            blocked_ip: Optional[BlockedIPs] = result.scalar()
            return BlockedIPRead.model_validate(blocked_ip) if blocked_ip else None

    async def create_blocked_ip(self, blocked_ip: BlockedIPCreate) -> Optional[BlockedIPRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                insert(BlockedIPs).values(
                    block=blocked_ip.block,
                    ip_address_v4=blocked_ip.ip_address_v4,
                    ip_address_v6=blocked_ip.ip_address_v6,
                    block_reason=blocked_ip.block_reason,
                ).returning(BlockedIPs)
            )
            ip: Optional[BlockedIPs] = result.scalar()
            return BlockedIPRead.model_validate(ip) if ip else None

    async def update_blocked_ip(self, blocked_ip: BlockedIPUpdate) -> Optional[BlockedIPRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(BlockedIPs)
                .where(BlockedIPs.id == blocked_ip.id)
                .values(
                    block=blocked_ip.block,
                    ip_address_v4=blocked_ip.ip_address_v4,
                    ip_address_v6=blocked_ip.ip_address_v6,
                    block_reason=blocked_ip.block_reason,
                )
                .returning(BlockedIPs)
            )
            updated_blocked_ip: Optional[BlockedIPs] = result.scalar()
            await s.commit()
            return BlockedIPRead.model_validate(updated_blocked_ip) if updated_blocked_ip else None

    async def delete_blocked_ip(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(delete(BlockedIPs).where(BlockedIPs.id == id))
            await s.commit()
