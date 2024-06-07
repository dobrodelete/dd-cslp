from typing import Optional, List

from sqlalchemy import select

from app.crud import CrudBase
from app.models import Like
from app.schemas import LikeCreate, LikeRead


class LikeCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_like(self, id: int) -> Optional[LikeRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Like).where(Like.id == id))
            like: Optional[Like] = result.scalar()
            return LikeRead.model_validate(like) if like else None

    async def get_likes(self, skip: int = 0, limit: int = 100) -> Optional[List[LikeRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Like).offset(skip).limit(limit))
            likes: Optional[List[Like]] = result.scalars().all()
            return [LikeRead.model_validate(like) for like in likes] if likes else None

    async def create_like(self, like: LikeCreate) -> Like:
        async with self.insert_session_scope() as s:
            db_like = Like(post_id=like.post_id, user_id=like.user_id)
            s.add(db_like)
            await s.flush()
            return db_like

    async def delete_like(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.delete(Like).where(Like.id == id)
