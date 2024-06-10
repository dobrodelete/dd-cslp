from typing import Optional, List
from sqlalchemy import select, update, delete
from app.crud import CrudBase
from app.models import TaskAssignment
from app.schemas import TaskAssignmentCreate, TaskAssignmentUpdate, TaskAssignmentRead


class TaskAssignmentCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_task_assignment(self, id: int) -> Optional[TaskAssignmentRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(TaskAssignment).where(TaskAssignment.id == id))
            task_assignment: Optional[TaskAssignment] = result.scalar()
            return TaskAssignmentRead.model_validate(task_assignment) if task_assignment else None

    async def get_task_assignments(self, skip: int = 0, limit: int = 100) -> Optional[List[TaskAssignmentRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(TaskAssignment).offset(skip).limit(limit))
            task_assignments: Optional[List[TaskAssignment]] = result.scalars().all()
            return [TaskAssignmentRead.model_validate(task_assignment) for task_assignment in task_assignments] if task_assignments else None

    async def create_task_assignment(self, task_assignment: TaskAssignmentCreate) -> TaskAssignment:
        async with self.insert_session_scope() as s:
            db_task_assignment = TaskAssignment(
                task_id=task_assignment.task_id,
                user_id=task_assignment.user_id
            )
            s.add(db_task_assignment)
            await s.flush()
            return db_task_assignment

    async def update_task_assignment(self, task_assignment: TaskAssignmentUpdate) -> Optional[TaskAssignmentRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(TaskAssignment)
                .where(TaskAssignment.id == task_assignment.id)
                .values(
                    task_id=task_assignment.task_id,
                    user_id=task_assignment.user_id
                )
                .returning(TaskAssignment)
            )
            updated_task_assignment: Optional[TaskAssignment] = result.scalar()
            return TaskAssignmentRead.model_validate(updated_task_assignment) if updated_task_assignment else None

    async def delete_task_assignment(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(delete(TaskAssignment).where(TaskAssignment.id == id))
