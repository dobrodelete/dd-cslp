from datetime import datetime
from typing import Optional

from pydantic import ConfigDict, BaseModel


class FileBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    filename: str
    filepath: str
    challenge_id: Optional[int] = None
    uploaded_at: datetime


class FileCreate(FileBase):
    pass


class FileRead(FileBase):
    id: int
    created_at: datetime
    updated_at: datetime


class FileUpdate(FileBase):
    id: int
