from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PageBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str
    content: str
    author_id: int
    published: bool


class PageCreate(PageBase):
    pass


class PageRead(PageBase):
    id: int
    created_at: datetime
    updated_at: datetime
    # media: List["MediaRead"] = []


class PageUpdate(PageRead):
    pass
