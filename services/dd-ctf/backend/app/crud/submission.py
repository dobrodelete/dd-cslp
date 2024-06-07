from typing import Optional, List
from sqlalchemy import select, update, delete
from app.crud.base import CrudBase
from app.models.submission import Submission
from app.schemas.submission import SubmissionCreate, SubmissionUpdate, SubmissionRead

class SubmissionCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_submission(self, id: int) -> Optional[SubmissionRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Submission).where(Submission.id == id))
            submission: Optional[Submission] = result.scalar()
            return SubmissionRead.model_validate(submission) if submission else None

    async def get_submissions(self, skip: int = 0, limit: int = 999) -> Optional[List[SubmissionRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Submission).offset(skip).limit(limit))
            submissions: Optional[List[Submission]] = result.scalars().all()
            return [SubmissionRead.model_validate(submission) for submission in submissions] if submissions else None

    async def create_submission(self, submission: SubmissionCreate) -> Submission:
        async with self.insert_session_scope() as s:
            db_submission = Submission(**submission.dict())
            s.add(db_submission)
            await s.flush()
            return db_submission

    async def update_submission(self, submission: SubmissionUpdate) -> Optional[SubmissionRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(Submission)
                .where(Submission.id == submission.id)
                .values(**submission.dict(exclude_unset=True))
                .returning(Submission)
            )
            submission: Optional[Submission] = result.scalar()
            return SubmissionRead.model_validate(submission) if submission else None

    async def delete_submission(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(
                delete(Submission)
                .where(Submission.id == id)
            )
