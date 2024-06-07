from pydantic import BaseModel, ConfigDict
from typing import Optional


class CategoryBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    description: Optional[str] = None


class CategoryCreate(CategoryBase):
    pass


class CategoryRead(CategoryBase):
    id: int


class CategoryUpdate(CategoryRead):
    pass
