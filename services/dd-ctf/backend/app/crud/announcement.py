from typing import Optional, List

from sqlalchemy import select, update, delete

from app.crud.base import CrudBase
from app.models.announcement import Announcement
from app.schemas.announcement import AnnouncementCreate, AnnouncementUpdate, AnnouncementRead


class AnnouncementCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_announcement(self, id: int) -> Optional[AnnouncementRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Announcement).where(Announcement.id == id))
            announcement: Optional[Announcement] = result.scalar()
            return AnnouncementRead.model_validate(announcement) if announcement else None

    async def get_announcements(self, skip: int = 0, limit: int = 999) -> Optional[List[AnnouncementRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Announcement).offset(skip).limit(limit))
            announcements: Optional[List[Announcement]] = result.scalars().all()
            return [AnnouncementRead.model_validate(announcement) for announcement in
                    announcements] if announcements else None

    async def create_announcement(self, announcement: AnnouncementCreate) -> Announcement:
        async with self.insert_session_scope() as s:
            db_announcement = Announcement(**announcement.dict())
            s.add(db_announcement)
            await s.flush()
            return db_announcement

    async def update_announcement(self, announcement: AnnouncementUpdate) -> Optional[AnnouncementRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(Announcement)
                .where(Announcement.id == announcement.id)
                .values(**announcement.dict(exclude_unset=True))
                .returning(Announcement)
            )
            announcement: Optional[Announcement] = result.scalar()
            return AnnouncementRead.model_validate(announcement) if announcement else None

    async def delete_announcement(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(
                delete(Announcement)
                .where(Announcement.id == id)
            )
