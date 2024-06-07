from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict


class PostBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str
    content: str
    category_id: int
    author_id: int
    published: bool


class PostCreate(PostBase):
    pass


class PostRead(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime
    # comments: List["CommentRead"] = []
    # likes: List["LikeRead"] = []
    # media: List["MediaRead"] = []
    # tags: List["TagRead"] = []


class PostUpdate(PostRead):
    pass
