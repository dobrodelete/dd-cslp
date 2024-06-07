from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TaskCommentBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    task_id: int
    author_id: int
    content: str


class TaskCommentCreate(TaskCommentBase):
    pass


class TaskCommentRead(TaskCommentBase):
    id: int
    created_at: datetime
