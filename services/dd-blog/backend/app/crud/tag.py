from typing import Optional, List

from sqlalchemy import select, update

from app.crud.base import CrudBase
from app.models import Tag
from app.schemas import TagCreate, TagUpdate, TagRead


class TagCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_tag(self, id: int) -> Optional[TagRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Tag).where(Tag.id == id))
            tag: Optional[Tag] = result.scalar()
            return TagRead.model_validate(tag) if tag else None

    async def get_tags(self, skip: int = 0, limit: int = 100) -> Optional[List[TagRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Tag).offset(skip).limit(limit))
            tags: Optional[List[Tag]] = result.scalars().all()
            return [TagRead.model_validate(tag) for tag in tags] if tags else None

    async def create_tag(self, tag: TagCreate) -> Tag:
        async with self.insert_session_scope() as s:
            db_tag = Tag(name=tag.name, description=tag.description)
            s.add(db_tag)
            await s.flush()
            return db_tag

    async def update_tag(self, tag: TagUpdate) -> Optional[TagRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(Tag)
                .where(Tag.id == tag.id)
                .values(name=tag.name, description=tag.description)
                .returning(Tag)
            )
            tag: Optional[Tag] = result.scalar()
            return TagRead.model_validate(tag) if tag else None

    async def delete_tag(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.delete(Tag).where(Tag.id == id)
