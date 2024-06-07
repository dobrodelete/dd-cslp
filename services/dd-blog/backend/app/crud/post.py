from typing import Optional, List

from sqlalchemy import select, update

from app.crud.base import CrudBase
from app.models import Post
from app.schemas import PostCreate, PostUpdate, PostRead


class PostCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_post(self, id: int) -> Optional[PostRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Post).where(Post.id == id))
            post: Optional[Post] = result.scalar()
            return PostRead.model_validate(post) if post else None

    async def get_posts(self, skip: int = 0, limit: int = 100) -> Optional[List[PostRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Post).offset(skip).limit(limit))
            posts: Optional[List[Post]] = result.scalars().all()
            return [PostRead.model_validate(post) for post in posts] if posts else None

    async def create_post(self, post: PostCreate) -> Post:
        async with self.insert_session_scope() as s:
            db_post = Post(
                title=post.title,
                content=post.content,
                category_id=post.category_id,
                author_id=post.author_id,
                published=post.published,
            )
            s.add(db_post)
            await s.flush()
            return db_post

    async def update_post(self, post: PostUpdate) -> Optional[PostRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(Post)
                .where(Post.id == post.id)
                .values(
                    title=post.title,
                    content=post.content,
                    published=post.published,
                )
                .returning(Post)
            )
            post: Optional[Post] = result.scalar()
            return PostRead.model_validate(post) if post else None

    async def delete_post(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.delete(Post).where(Post.id == id)
