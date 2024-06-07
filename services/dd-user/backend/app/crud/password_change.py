from typing import Optional, List

from sqlalchemy import select, update, delete

from app.crud import CrudBase
from app.models import PasswordChanges
from app.schemas import PasswordChangeCreate, PasswordChangeUpdate, PasswordChangeRead


class PasswordChangeCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_password_change(self, id: int) -> Optional[PasswordChangeRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(PasswordChanges).where(PasswordChanges.id == id))
            password_change: Optional[PasswordChanges] = result.scalar()
            return PasswordChangeRead.model_validate(password_change) if password_change else None

    async def get_password_changes(self, skip: int = 0, limit: int = 999) -> Optional[List[PasswordChangeRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(PasswordChanges).offset(skip).limit(limit))
            password_changes: Optional[List[PasswordChanges]] = result.scalars().all()
            return [PasswordChangeRead.model_validate(password_change) for password_change in
                    password_changes] if password_changes else None

    async def create_password_change(self, password_change: PasswordChangeCreate) -> PasswordChanges:
        async with self.insert_session_scope() as s:
            db_password_change = PasswordChanges(
                user_id=password_change.user_id,
                old_password_hash=password_change.old_password_hash,
                new_password_hash=password_change.new_password_hash,
                change_time=password_change.change_time,
            )
            s.add(db_password_change)
            await s.flush()
            return db_password_change

    async def update_password_change(self, password_change: PasswordChangeUpdate) -> Optional[PasswordChangeRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(PasswordChanges)
                .where(PasswordChanges.id == password_change.id)
                .values(
                    user_id=password_change.user_id,
                    old_password_hash=password_change.old_password_hash,
                    new_password_hash=password_change.new_password_hash,
                    change_time=password_change.change_time,
                )
                .returning(PasswordChanges)
            )
            updated_password_change: Optional[PasswordChanges] = result.scalar()
            return PasswordChangeRead.model_validate(updated_password_change) if updated_password_change else None

    async def delete_password_change(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(delete(PasswordChanges).where(PasswordChanges.id == id))
