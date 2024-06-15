from typing import Optional, List

from sqlalchemy import select, update, delete

from app.crud import CrudBase
from app.models import Link
from app.schemas import LinkRead, LinkCreate, LinkUpdate


class LinkCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_link(self, id: int) -> Optional[LinkRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Link).where(Link.id == id))
            link: Optional[Link] = result.scalar()
            return LinkRead.model_validate(link) if link else None

    async def get_links(self, skip: int = 0, limit: int = 999) -> Optional[List[LinkRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Link).offset(skip).limit(limit))
            links: Optional[List[Link]] = result.scalars().all()
            return [LinkRead.model_validate(link) for link in links] if links else None

    async def create_link(self, link: LinkCreate) -> Link:
        async with self.insert_session_scope() as s:
            db_link = Link(
                url=link.url,
                description=link.description,
                challenge_id=link.challenge_id,
                created_at=link.created_at,
            )
            s.add(db_link)
            await s.flush()
            return db_link

    async def update_link(self, link: LinkUpdate) -> Optional[LinkRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(Link)
                .where(Link.id == link.id)
                .values(
                    url=link.url,
                    description=link.description,
                    challenge_id=link.challenge_id,
                    created_at=link.created_at,
                )
                .returning(Link)
            )
            updated_link: Optional[Link] = result.scalar()
            return LinkRead.model_validate(updated_link) if updated_link else None

    async def delete_link(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(delete(Link).where(Link.id == id))
