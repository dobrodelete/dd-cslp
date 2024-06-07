from typing import Optional, List

from sqlalchemy import select, insert
from sqlalchemy.orm import selectinload

from app.crud.base import CrudBase
from app.models import Role, Permission
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate, UserRead


class UserCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_all_users_with_data(self, limit: int = 999, offset: int = 0) -> Optional[List[UserRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(
                select(User)
                .options(selectinload(User.roles).options(Role.permissions))
                .options(selectinload(User.permissions).options(Permission.roles))
                .options(selectinload(User.login_attempts))
                .options(selectinload(User.password_changes))
                .options(selectinload(User.user_access_log))
                .options(selectinload(User.user_security))
                .options(selectinload(User.user_session))
                .options(selectinload(User.user_settings))
                .limit(limit=limit)
                .offset(offset=offset)
                .order_by(User.id)
            )
            users: Optional[List[User]] = result.scalars().all()
            return [UserRead.model_validate(user) for user in users]

    async def get_user(self, id: int) -> Optional[UserRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(User).filter(User.id == id))
            user: Optional[User] = result.scalar().one_or_none()
            return UserRead.model_validate(user) if user else None

    async def get_user_by_email(self, email: str) -> Optional[User]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(User).filter(User.email == email))
            return result.scalar_one_or_none()

    async def get_user_by_username(self, username: str) -> Optional[UserRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(User).filter(User.username == username))
            user: Optional[User] = result.scalar()
            return UserRead.model_validate(user) if user else None

    async def create_user(self, user: UserCreate) -> Optional[UserRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(insert(User).values(
                username=user.username,
                email=user.email,
                password_hash=user.password_hash,
                full_name=user.full_name,
                phone_number=user.phone_number,
                is_admin=user.is_admin,
                is_active=user.is_active,
            ).returning(User))
            user: Optional[User] = result.scalar()
            return UserRead.model_validate(user) if user else None

    async def update_user(self, db_user: User, user_update: UserUpdate) -> User:
        async with self.insert_session_scope() as s:
            for var, value in vars(user_update).items():
                setattr(db_user, var, value) if value else None
            s.add(db_user)
            await s.flush()
            return db_user

    async def delete_user(self, user_id: int) -> Optional[User]:
        async with self.insert_session_scope() as s:
            db_user = await self.get_user(user_id)
            if db_user:
                await s.delete(db_user)
                await s.flush()
            return db_user
