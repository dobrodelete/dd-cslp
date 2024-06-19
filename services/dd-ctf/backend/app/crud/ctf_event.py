from typing import Optional, List

from sqlalchemy import select, update, delete, func

from app.crud import CrudBase
from app.models import CTFEvent
from app.schemas import CTFEventRead, CTFEventCreate, CTFEventUpdate


class CTFEventCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_ctf_event(self, id: int) -> Optional[CTFEventRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(CTFEvent).where(CTFEvent.id == id))
            ctf_event: Optional[CTFEvent] = result.scalar()
            return CTFEventRead.model_validate(ctf_event) if ctf_event else None

    async def get_ctf_events(self, skip: int = 0, limit: int = 999) -> Optional[List[CTFEventRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(CTFEvent).offset(skip).limit(limit))
            ctf_events: Optional[List[CTFEvent]] = result.scalars().all()
            return [CTFEventRead.model_validate(ctf_event) for ctf_event in ctf_events] if ctf_events else None

    async def create_ctf_event(self, ctf_event: CTFEventCreate) -> CTFEvent:
        async with self.insert_session_scope() as s:
            db_ctf_event = CTFEvent(
                name=ctf_event.name,
                description=ctf_event.description,
                start_time=ctf_event.start_time.replace(tzinfo=None),
                end_time=ctf_event.end_time.replace(tzinfo=None),
                active=ctf_event.active,
            )
            s.add(db_ctf_event)
            await s.flush()
            return db_ctf_event

    async def update_ctf_event(self, ctf_event: CTFEventUpdate) -> Optional[CTFEventRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(CTFEvent)
                .where(CTFEvent.id == ctf_event.id)
                .values(
                    name=ctf_event.name,
                    description=ctf_event.description,
                    start_time=ctf_event.start_time.replace(tzinfo=None),
                    end_time=ctf_event.end_time.replace(tzinfo=None),
                    active=ctf_event.active,
                )
                .returning(CTFEvent)
            )
            updated_ctf_event: Optional[CTFEvent] = result.scalar()
            return CTFEventRead.model_validate(updated_ctf_event) if updated_ctf_event else None

    async def delete_ctf_event(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(delete(CTFEvent).where(CTFEvent.id == id))

    async def get_total(self, ) -> int:
        async with self.read_session_scope() as s:
            result = await s.execute(select(func.count("*")).select_from(CTFEvent))
            count = result.scalar()
            return count
