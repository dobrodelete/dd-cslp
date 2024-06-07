from typing import Optional, List

from sqlalchemy import select, update

from app.crud.base import CrudBase
from app.models import Page
from app.schemas import PageCreate, PageUpdate, PageRead


class PageCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_page(self, id: int) -> Optional[PageRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Page).where(Page.id == id))
            page: Optional[Page] = result.scalar()
            return PageRead.model_validate(page) if page else None

    async def get_pages(self, skip: int = 0, limit: int = 100) -> Optional[List[PageRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Page).offset(skip).limit(limit))
            pages: Optional[List[Page]] = result.scalars().all()
            return [PageRead.model_validate(page) for page in pages] if pages else None

    async def create_page(self, page: PageCreate) -> Page:
        async with self.insert_session_scope() as s:
            db_page = Page(
                title=page.title,
                content=page.content,
                author_id=page.author_id,
                published=page.published,
            )
            s.add(db_page)
            await s.flush()
            return db_page

    async def update_page(self, page: PageUpdate) -> Optional[PageRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(Page)
                .where(Page.id == page.id)
                .values(
                    title=page.title,
                    content=page.content,
                    published=page.published,
                )
                .returning(Page)
            )
            page: Optional[Page] = result.scalar()
            return PageRead.model_validate(page) if page else None

    async def delete_page(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.delete(Page).where(Page.id == id)
