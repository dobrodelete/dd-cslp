from typing import Optional, List

from sqlalchemy import select, update, delete

from app.crud import CrudBase
from app.models import UserAccessLog
from app.schemas import UserAccessLogCreate, UserAccessLogUpdate, UserAccessLogRead


class UserAccessLogCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_user_access_log(self, id: int) -> Optional[UserAccessLogRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(UserAccessLog).where(UserAccessLog.id == id))
            user_access_log: Optional[UserAccessLog] = result.scalar()
            return UserAccessLogRead.model_validate(user_access_log) if user_access_log else None

    async def get_user_access_logs(self, skip: int = 0, limit: int = 999) -> Optional[List[UserAccessLogRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(UserAccessLog).offset(skip).limit(limit))
            user_access_logs: Optional[List[UserAccessLog]] = result.scalars().all()
            return [UserAccessLogRead.model_validate(user_access_log) for user_access_log in
                    user_access_logs] if user_access_logs else None

    async def create_user_access_log(self, user_access_log: UserAccessLogCreate) -> UserAccessLog:
        async with self.insert_session_scope() as s:
            db_user_access_log = UserAccessLog(
                user_id=user_access_log.user_id,
                timestamp=user_access_log.timestamp,
                ip_address=user_access_log.ip_address,
                action=user_access_log.action,
                status=user_access_log.status,
                user_agent=user_access_log.user_agent,
                location=user_access_log.location,
            )
            s.add(db_user_access_log)
            await s.flush()
            return db_user_access_log

    async def update_user_access_log(self, user_access_log: UserAccessLogUpdate) -> Optional[UserAccessLogRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(UserAccessLog)
                .where(UserAccessLog.id == user_access_log.id)
                .values(
                    user_id=user_access_log.user_id,
                    timestamp=user_access_log.timestamp,
                    ip_address=user_access_log.ip_address,
                    action=user_access_log.action,
                    status=user_access_log.status,
                    user_agent=user_access_log.user_agent,
                    location=user_access_log.location,
                )
                .returning(UserAccessLog)
            )
            updated_user_access_log: Optional[UserAccessLog] = result.scalar()
            return UserAccessLogRead.model_validate(updated_user_access_log) if updated_user_access_log else None

    async def delete_user_access_log(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(delete(UserAccessLog).where(UserAccessLog.id == id))
