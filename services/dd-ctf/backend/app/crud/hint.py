from typing import Optional, List
from sqlalchemy import select, update, delete
from app.crud.base import CrudBase
from app.models.hint import Hint
from app.schemas.hint import HintCreate, HintUpdate, HintRead


class HintCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_hint(self, id: int) -> Optional[HintRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Hint).where(Hint.id == id))
            hint: Optional[Hint] = result.scalar()
            return HintRead.model_validate(hint) if hint else None

    async def get_hints(self, skip: int = 0, limit: int = 999) -> Optional[List[HintRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Hint).offset(skip).limit(limit))
            hints: Optional[List[Hint]] = result.scalars().all()
            return [HintRead.model_validate(hint) for hint in hints] if hints else None

    async def create_hint(self, hint: HintCreate) -> Hint:
        async with self.insert_session_scope() as s:
            db_hint = Hint(**hint.dict())
            s.add(db_hint)
            await s.flush()
            return db_hint

    async def update_hint(self, hint: HintUpdate) -> Optional[HintRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(Hint)
                .where(Hint.id == hint.id)
                .values(**hint.dict(exclude_unset=True))
                .returning(Hint)
            )
            hint: Optional[Hint] = result.scalar()
            return HintRead.model_validate(hint) if hint else None

    async def delete_hint(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(
                delete(Hint)
                .where(Hint.id == id)
            )
