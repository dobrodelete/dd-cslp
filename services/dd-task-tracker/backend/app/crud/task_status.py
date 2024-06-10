from typing import Optional, List
from sqlalchemy import select, update, delete
from app.crud import CrudBase
from app.models import TaskStatus
from app.schemas import TaskStatusCreate, TaskStatusUpdate, TaskStatusRead


class TaskStatusCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_task_status(self, id: int) -> Optional[TaskStatusRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(TaskStatus).where(TaskStatus.id == id))
            task_status: Optional[TaskStatus] = result.scalar()
            return TaskStatusRead.model_validate(task_status) if task_status else None

    async def get_task_statuses(self, skip: int = 0, limit: int = 100) -> Optional[List[TaskStatusRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(TaskStatus).offset(skip).limit(limit))
            task_statuses: Optional[List[TaskStatus]] = result.scalars().all()
            return [TaskStatusRead.model_validate(task_status) for task_status in task_statuses] if task_statuses else None

    async def create_task_status(self, task_status: TaskStatusCreate) -> TaskStatus:
        async with self.insert_session_scope() as s:
            db_task_status = TaskStatus(
                name=task_status.name,
                description=task_status.description
            )
            s.add(db_task_status)
            await s.flush()
            return db_task_status

    async def update_task_status(self, task_status: TaskStatusUpdate) -> Optional[TaskStatusRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(TaskStatus)
                .where(TaskStatus.id == task_status.id)
                .values(
                    name=task_status.name,
                    description=task_status.description
                )
                .returning(TaskStatus)
            )
            updated_task_status: Optional[TaskStatus] = result.scalar()
            return TaskStatusRead.model_validate(updated_task_status) if updated_task_status else None

    async def delete_task_status(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(delete(TaskStatus).where(TaskStatus.id == id))
