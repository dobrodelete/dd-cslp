from pydantic import BaseModel, ConfigDict
from typing import Optional


class TaskStatusBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    description: Optional[str] = None


class TaskStatusCreate(TaskStatusBase):
    pass


class TaskStatusRead(TaskStatusBase):
    id: int


class TaskStatusUpdate(TaskStatusRead):
    pass
