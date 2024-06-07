from typing import Optional, List

from sqlalchemy import select, delete

from app.crud import CrudBase
from app.models import LoginAttempts
from app.schemas import LoginAttemptCreate, LoginAttemptRead


class LoginAttemptCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_login_attempt(self, id: int) -> Optional[LoginAttemptRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(LoginAttempts).where(LoginAttempts.id == id))
            login_attempt: Optional[LoginAttempts] = result.scalar()
            return LoginAttemptRead.model_validate(login_attempt) if login_attempt else None

    async def get_login_attempts(self, skip: int = 0, limit: int = 999) -> Optional[List[LoginAttemptRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(LoginAttempts).offset(skip).limit(limit))
            login_attempts: Optional[List[LoginAttempts]] = result.scalars().all()
            return [LoginAttemptRead.model_validate(login_attempt) for login_attempt in
                    login_attempts] if login_attempts else None

    async def create_login_attempt(self, login_attempt: LoginAttemptCreate) -> LoginAttempts:
        async with self.insert_session_scope() as s:
            db_login_attempt = LoginAttempts(
                user_id=login_attempt.user_id,
                attempt_time=login_attempt.attempt_time,
                ip_address_v4=login_attempt.ip_address_v4,
                ip_address_v6=login_attempt.ip_address_v6,
                user_agent=login_attempt.user_agent,
                successful=login_attempt.successful,
            )
            s.add(db_login_attempt)
            await s.flush()
            return db_login_attempt

    async def delete_login_attempt(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(delete(LoginAttempts).where(LoginAttempts.id == id))
