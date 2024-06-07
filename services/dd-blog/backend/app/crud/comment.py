from typing import Optional, List

from sqlalchemy import select, update

from app.crud import CrudBase
from app.models import Comment
from app.schemas import CommentCreate, CommentUpdate, CommentRead


class CommentCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_comment(self, id: int) -> Optional[CommentRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Comment).where(Comment.id == id))
            comment: Optional[Comment] = result.scalar()
            return CommentRead.model_validate(comment) if comment else None

    async def get_comments(self, skip: int = 0, limit: int = 100) -> Optional[List[CommentRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Comment).offset(skip).limit(limit))
            comments: Optional[List[Comment]] = result.scalars().all()
            return [CommentRead.model_validate(comment) for comment in comments] if comments else None

    async def create_comment(self, comment: CommentCreate) -> Comment:
        async with self.insert_session_scope() as s:
            db_comment = Comment(post_id=comment.post_id, author_id=comment.author_id, content=comment.content)
            s.add(db_comment)
            await s.flush()
            return db_comment

    async def update_comment(self, comment: CommentUpdate) -> Optional[CommentRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(Comment)
                .where(Comment.id == comment.id)
                .values(post_id=comment.post_id, author_id=comment.author_id, content=comment.content)
                .returning(Comment)
            )
            comment: Optional[Comment] = result.scalar()
            return CommentRead.model_validate(comment) if comment else None

    async def delete_comment(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.delete(Comment).where(Comment.id == id)
