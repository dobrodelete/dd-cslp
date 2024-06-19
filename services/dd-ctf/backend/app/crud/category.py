from typing import Optional, List

from sqlalchemy import select, update, delete, insert, func

from app.crud import CrudBase
from app.models import Category
from app.schemas import CategoryCreate, CategoryUpdate, CategoryRead


class CategoryCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_category(self, id: int) -> Optional[CategoryRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Category).where(Category.id == id))
            category: Optional[Category] = result.scalar()
            return CategoryRead.model_validate(category) if category else None

    async def get_categories(self, skip: int = 0, limit: int = 999) -> Optional[List[CategoryRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Category).offset(skip).limit(limit))
            categories: Optional[List[Category]] = result.scalars().all()
            return [CategoryRead.model_validate(category) for category in categories] if categories else None

    async def create_category(self, category: CategoryCreate) -> Optional[CategoryRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                insert(Category).values(
                    **category.dict()
                ).returning(Category))
            return_category: Optional[Category] = result.scalar_one_or_none()
            return CategoryRead.model_validate(return_category) if return_category else None

    async def update_category(self, category: CategoryUpdate) -> Optional[CategoryRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(Category)
                .where(Category.id == category.id)
                .values(**category.dict(exclude_unset=True))
                .returning(Category)
            )
            category: Optional[Category] = result.scalar()
            return CategoryRead.model_validate(category) if category else None

    async def delete_category(self, id: int) -> bool:
        async with self.insert_session_scope() as s:
            await s.execute(
                delete(Category)
                .where(Category.id == id)
            )
            return True

    async def get_total(self, ) -> int:
        async with self.read_session_scope() as s:
            result = await s.execute(select(func.count("*")).select_from(Category))
            count = result.scalar()
            return count
