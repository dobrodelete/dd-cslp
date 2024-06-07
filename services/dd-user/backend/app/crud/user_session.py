from typing import Optional, List

from sqlalchemy import select, update, delete, insert

from app.crud import CrudBase
from app.models import UserSession
from app.schemas import UserSessionCreate, UserSessionUpdate, UserSessionRead


class UserSessionCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_user_session(self, id: int) -> Optional[UserSessionRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(UserSession).where(UserSession.id == id))
            user_session: Optional[UserSession] = result.scalar()
            return UserSessionRead.model_validate(user_session) if user_session else None

    async def get_user_sessions(self, skip: int = 0, limit: int = 999) -> Optional[List[UserSessionRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(UserSession).offset(skip).limit(limit))
            user_sessions: Optional[List[UserSession]] = result.scalars().all()
            return [UserSessionRead.model_validate(user_session) for user_session in
                    user_sessions] if user_sessions else None

    async def create_user_session(self, user_session: UserSessionCreate) -> Optional[UserSessionRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(insert(UserSession).values(
                user_id=user_session.user_id,
                session_token=user_session.session_token,
                expires_at=user_session.expires_at,
                ip_address=user_session.ip_address,
                user_agent=user_session.user_agent
            ).returning(UserSession))
            session: Optional[UserSession] = result.scalar()
            return UserSessionRead.model_validate(session) if session else None

    async def update_user_session(self, user_session: UserSessionUpdate) -> Optional[UserSessionRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(UserSession)
                .where(UserSession.id == user_session.id)
                .values(
                    user_id=user_session.user_id,
                    session_token=user_session.session_token,
                    created_at=user_session.created_at,
                    expires_at=user_session.expires_at,
                    ip_address=user_session.ip_address,
                    user_agent=user_session.user_agent,
                )
                .returning(UserSession)
            )
            updated_user_session: Optional[UserSession] = result.scalar()
            return UserSessionRead.model_validate(updated_user_session) if updated_user_session else None

    async def delete_user_session(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(delete(UserSession).where(UserSession.id == id))
