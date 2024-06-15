from typing import Optional, List

from sqlalchemy import select, update, delete

from app.crud import CrudBase
from app.models import ChallengeComment
from app.schemas import ChallengeCommentRead, ChallengeCommentCreate, ChallengeCommentUpdate


class ChallengeCommentCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_comment(self, id: int) -> Optional[ChallengeCommentRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(ChallengeComment).where(ChallengeComment.id == id))
            comment: Optional[ChallengeComment] = result.scalar()
            return ChallengeCommentRead.model_validate(comment) if comment else None

    async def get_comments(self, skip: int = 0, limit: int = 999) -> Optional[List[ChallengeCommentRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(ChallengeComment).offset(skip).limit(limit))
            comments: Optional[List[ChallengeComment]] = result.scalars().all()
            return [ChallengeCommentRead.model_validate(comment) for comment in comments] if comments else None

    async def create_comment(self, comment: ChallengeCommentCreate) -> ChallengeComment:
        async with self.insert_session_scope() as s:
            db_comment = ChallengeComment(
                challenge_id=comment.challenge_id,
                user_id=comment.user_id,
                content=comment.content,
            )
            s.add(db_comment)
            await s.flush()
            return db_comment

    async def update_comment(self, comment: ChallengeCommentUpdate) -> Optional[ChallengeCommentRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(ChallengeComment)
                .where(ChallengeComment.id == comment.id)
                .values(
                    challenge_id=comment.challenge_id,
                    user_id=comment.user_id,
                    content=comment.content,
                )
                .returning(ChallengeComment)
            )
            updated_comment: Optional[ChallengeComment] = result.scalar()
            return ChallengeCommentRead.model_validate(updated_comment) if updated_comment else None

    async def delete_comment(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(delete(ChallengeComment).where(ChallengeComment.id == id))
