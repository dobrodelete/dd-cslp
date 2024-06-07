from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str
    description: Optional[str] = None
    project_id: int
    status_id: int
    due_date: Optional[datetime] = None


class TaskCreate(TaskBase):
    pass


class TaskRead(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime
    comments: List["TaskCommentRead"] = []
    assignments: List["TaskAssignmentRead"] = []
