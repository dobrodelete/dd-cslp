from typing import Optional, List
from sqlalchemy import select, update, delete
from app.crud import CrudBase
from app.models import TaskComment
from app.schemas import TaskCommentCreate, TaskCommentUpdate, TaskCommentRead


class TaskCommentCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_task_comment(self, id: int) -> Optional[TaskCommentRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(TaskComment).where(TaskComment.id == id))
            task_comment: Optional[TaskComment] = result.scalar()
            return TaskCommentRead.model_validate(task_comment) if task_comment else None

    async def get_task_comments(self, skip: int = 0, limit: int = 100) -> Optional[List[TaskCommentRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(TaskComment).offset(skip).limit(limit))
            task_comments: Optional[List[TaskComment]] = result.scalars().all()
            return [TaskCommentRead.model_validate(task_comment) for task_comment in task_comments] if task_comments else None

    async def create_task_comment(self, task_comment: TaskCommentCreate) -> TaskComment:
        async with self.insert_session_scope() as s:
            db_task_comment = TaskComment(
                task_id=task_comment.task_id,
                author_id=task_comment.author_id,
                content=task_comment.content
            )
            s.add(db_task_comment)
            await s.flush()
            return db_task_comment

    async def update_task_comment(self, task_comment: TaskCommentUpdate) -> Optional[TaskCommentRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(TaskComment)
                .where(TaskComment.id == task_comment.id)
                .values(
                    task_id=task_comment.task_id,
                    author_id=task_comment.author_id,
                    content=task_comment.content
                )
                .returning(TaskComment)
            )
            updated_task_comment: Optional[TaskComment] = result.scalar()
            return TaskCommentRead.model_validate(updated_task_comment) if updated_task_comment else None

    async def delete_task_comment(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(delete(TaskComment).where(TaskComment.id == id))
