from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TaskAssignmentBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    task_id: int
    user_id: int


class TaskAssignmentCreate(TaskAssignmentBase):
    pass


class TaskAssignmentRead(TaskAssignmentBase):
    id: int
    assigned_at: datetime
