from typing import Optional, List

from sqlalchemy import select, update

from app.crud import CrudBase
from app.models import Media
from app.schemas import MediaCreate, MediaUpdate, MediaRead


class MediaCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_media(self, id: int) -> Optional[MediaRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Media).where(Media.id == id))
            media: Optional[Media] = result.scalar()
            return MediaRead.model_validate(media) if media else None

    async def get_medias(self, skip: int = 0, limit: int = 100) -> Optional[List[MediaRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Media).offset(skip).limit(limit))
            medias: Optional[List[Media]] = result.scalars().all()
            return [MediaRead.model_validate(media) for media in medias] if medias else None

    async def create_media(self, media: MediaCreate) -> Media:
        async with self.insert_session_scope() as s:
            db_media = Media(url=media.url, post_id=media.post_id, page_id=media.page_id)
            s.add(db_media)
            await s.flush()
            return db_media

    async def update_media(self, media: MediaUpdate) -> Optional[MediaRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(Media)
                .where(Media.id == media.id)
                .values(url=media.url, post_id=media.post_id, page_id=media.page_id)
                .returning(Media)
            )
            media: Optional[Media] = result.scalar()
            return MediaRead.model_validate(media) if media else None

    async def delete_media(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.delete(Media).where(Media.id == id)
