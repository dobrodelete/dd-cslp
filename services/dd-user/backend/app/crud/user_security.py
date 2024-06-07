from typing import Optional, List

from sqlalchemy import select, update, delete

from app.crud import CrudBase
from app.models import UserSecurity
from app.schemas import UserSecurityCreate, UserSecurityUpdate, UserSecurityRead


class UserSecurityCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_user_security(self, id: int) -> Optional[UserSecurityRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(UserSecurity).where(UserSecurity.id == id))
            user_security: Optional[UserSecurity] = result.scalar()
            return UserSecurityRead.model_validate(user_security) if user_security else None

    async def get_user_securities(self, skip: int = 0, limit: int = 999) -> Optional[List[UserSecurityRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(UserSecurity).offset(skip).limit(limit))
            user_securities: Optional[List[UserSecurity]] = result.scalars().all()
            return [UserSecurityRead.model_validate(user_security) for user_security in
                    user_securities] if user_securities else None

    async def create_user_security(self, user_security: UserSecurityCreate) -> UserSecurity:
        async with self.insert_session_scope() as s:
            db_user_security = UserSecurity(
                user_id=user_security.user_id,
                last_login=user_security.last_login,
                login_attempts=user_security.login_attempts,
                last_failed_login=user_security.last_failed_login,
                password_changed_at=user_security.password_changed_at,
                password_reset_token=user_security.password_reset_token,
                password_reset_token_expires_at=user_security.password_reset_token_expires_at,
                account_lock=user_security.account_lock,
                account_lock_until=user_security.account_lock_until,
            )
            s.add(db_user_security)
            await s.flush()
            return db_user_security

    async def update_user_security(self, user_security: UserSecurityUpdate) -> Optional[UserSecurityRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(UserSecurity)
                .where(UserSecurity.id == user_security.id)
                .values(
                    user_id=user_security.user_id,
                    last_login=user_security.last_login,
                    login_attempts=user_security.login_attempts,
                    last_failed_login=user_security.last_failed_login,
                    password_changed_at=user_security.password_changed_at,
                    password_reset_token=user_security.password_reset_token,
                    password_reset_token_expires_at=user_security.password_reset_token_expires_at,
                    account_lock=user_security.account_lock,
                    account_lock_until=user_security.account_lock_until,
                )
                .returning(UserSecurity)
            )
            updated_user_security: Optional[UserSecurity] = result.scalar()
            return UserSecurityRead.model_validate(updated_user_security) if updated_user_security else None

    async def delete_user_security(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(delete(UserSecurity).where(UserSecurity.id == id))
