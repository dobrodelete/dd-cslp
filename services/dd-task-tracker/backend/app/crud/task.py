from typing import Optional, List
from sqlalchemy import select, update, delete
from app.crud import CrudBase
from app.models import Task
from app.schemas import TaskCreate, TaskUpdate, TaskRead


class TaskCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_task(self, id: int) -> Optional[TaskRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Task).where(Task.id == id))
            task: Optional[Task] = result.scalar()
            return TaskRead.model_validate(task) if task else None

    async def get_tasks(self, skip: int = 0, limit: int = 100) -> Optional[List[TaskRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Task).offset(skip).limit(limit))
            tasks: Optional[List[Task]] = result.scalars().all()
            return [TaskRead.model_validate(task) for task in tasks] if tasks else None

    async def create_task(self, task: TaskCreate) -> Task:
        async with self.insert_session_scope() as s:
            db_task = Task(
                title=task.title,
                description=task.description,
                project_id=task.project_id,
                status_id=task.status_id,
                due_date=task.due_date
            )
            s.add(db_task)
            await s.flush()
            return db_task

    async def update_task(self, task: TaskUpdate) -> Optional[TaskRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(Task)
                .where(Task.id == task.id)
                .values(
                    title=task.title,
                    description=task.description,
                    project_id=task.project_id,
                    status_id=task.status_id,
                    due_date=task.due_date
                )
                .returning(Task)
            )
            updated_task: Optional[Task] = result.scalar()
            return TaskRead.model_validate(updated_task) if updated_task else None

    async def delete_task(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(delete(Task).where(Task.id == id))
