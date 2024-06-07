from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CommentBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    post_id: int
    author_id: int
    content: str


class CommentCreate(CommentBase):
    pass


class CommentRead(CommentBase):
    id: int
    created_at: datetime


class CommentUpdate(CommentRead):
    pass
