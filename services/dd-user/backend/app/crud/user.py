from typing import Optional, List

from sqlalchemy import select, insert, update, delete
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
                .options(selectinload(User.roles).selectinload(Role.permissions))
                .options(selectinload(User.permissions).selectinload(Permission.roles))
                .options(selectinload(User.login_attempts))
                .options(selectinload(User.password_changes))
                .options(selectinload(User.user_access_log))
                .options(selectinload(User.user_security))
                .options(selectinload(User.user_session))
                .options(selectinload(User.user_settings))
                .limit(limit)
                .offset(offset)
                .order_by(User.id)
            )
            users: Optional[List[User]] = result.scalars().all()
            return [UserRead.model_validate(user) for user in users] if users else None

    async def get_user(self, id: int) -> Optional[UserRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(
                select(User)
                .options(selectinload(User.roles).selectinload(Role.permissions))
                .options(selectinload(User.permissions).selectinload(Permission.roles))
                .options(selectinload(User.login_attempts))
                .options(selectinload(User.password_changes))
                .options(selectinload(User.user_access_log))
                .options(selectinload(User.user_security))
                .options(selectinload(User.user_session))
                .options(selectinload(User.user_settings))
                .filter(User.id == id)
            )
            user: Optional[User] = result.scalar_one_or_none()
            return UserRead.model_validate(user) if user else None

    async def get_user_by_email(self, email: str) -> Optional[UserRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(
                select(User)
                .options(selectinload(User.roles).selectinload(Role.permissions))
                .options(selectinload(User.permissions).selectinload(Permission.roles))
                .options(selectinload(User.login_attempts))
                .options(selectinload(User.password_changes))
                .options(selectinload(User.user_access_log))
                .options(selectinload(User.user_security))
                .options(selectinload(User.user_session))
                .options(selectinload(User.user_settings))
                .filter(User.email == email)
            )
            user: Optional[User] = result.scalar_one_or_none()
            return UserRead.model_validate(user) if user else None

    async def get_user_by_username(self, username: str) -> Optional[UserRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(
                select(User)
                .options(selectinload(User.roles).selectinload(Role.permissions))
                .options(selectinload(User.permissions).selectinload(Permission.roles))
                .options(selectinload(User.login_attempts))
                .options(selectinload(User.password_changes))
                .options(selectinload(User.user_access_log))
                .options(selectinload(User.user_security))
                .options(selectinload(User.user_session))
                .options(selectinload(User.user_settings))
                .filter(User.username == username)
            )
            user: Optional[User] = result.scalar_one_or_none()
            return UserRead.model_validate(user) if user else None

    async def create_user(self, user: UserCreate) -> Optional[UserRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                insert(User).values(
                    username=user.username,
                    email=user.email,
                    password_hash=user.password_hash,
                    full_name=user.full_name,
                    phone_number=user.phone_number,
                    is_admin=user.is_admin,
                    is_active=user.is_active
                ).returning(User)
            )
            user: Optional[User] = result.scalar_one_or_none()
            return UserRead.model_validate(user) if user else None

    async def update_user(self, id: int, user_update: UserUpdate) -> Optional[UserRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(User)
                .where(User.id == id)
                .values(user_update.dict(exclude_unset=True))
                .returning(User)
            )
            updated_user: Optional[User] = result.scalar_one_or_none()
            return UserRead.model_validate(updated_user) if updated_user else None

    async def delete_user(self, id: int) -> Optional[UserRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                delete(User)
                .where(User.id == id)
                .returning(User)
            )
            deleted_user: Optional[User] = result.scalar_one_or_none()
            return UserRead.model_validate(deleted_user) if deleted_user else None
