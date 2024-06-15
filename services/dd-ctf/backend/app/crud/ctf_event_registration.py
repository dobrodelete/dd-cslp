from typing import Optional, List

from sqlalchemy import select, update, delete

from app.crud import CrudBase
from app.models import CTFEventRegistration
from app.schemas import CTFEventRegistrationRead, CTFEventRegistrationCreate, CTFEventRegistrationUpdate


class CTFEventRegistrationCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_registration(self, id: int) -> Optional[CTFEventRegistrationRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(CTFEventRegistration).where(CTFEventRegistration.id == id))
            registration: Optional[CTFEventRegistration] = result.scalar()
            return CTFEventRegistrationRead.model_validate(registration) if registration else None

    async def get_registrations(self, skip: int = 0, limit: int = 999) -> Optional[List[CTFEventRegistrationRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(CTFEventRegistration).offset(skip).limit(limit))
            registrations: Optional[List[CTFEventRegistration]] = result.scalars().all()
            return [CTFEventRegistrationRead.model_validate(registration) for registration in
                    registrations] if registrations else None

    async def create_registration(self, registration: CTFEventRegistrationCreate) -> CTFEventRegistration:
        async with self.insert_session_scope() as s:
            db_registration = CTFEventRegistration(
                user_id=registration.user_id,
                event_id=registration.event_id,
                registered_at=registration.registered_at,
            )
            s.add(db_registration)
            await s.flush()
            return db_registration

    async def update_registration(self, registration: CTFEventRegistrationUpdate) -> Optional[CTFEventRegistrationRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(CTFEventRegistration)
                .where(CTFEventRegistration.id == registration.id)
                .values(
                    user_id=registration.user_id,
                    event_id=registration.event_id,
                    registered_at=registration.registered_at,
                )
                .returning(CTFEventRegistration)
            )
            updated_registration: Optional[CTFEventRegistration] = result.scalar()
            return CTFEventRegistrationRead.model_validate(updated_registration) if updated_registration else None

    async def delete_registration(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(delete(CTFEventRegistration).where(CTFEventRegistration.id == id))
