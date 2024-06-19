from typing import Optional, List

from sqlalchemy import select, update, delete

from app.crud import CrudBase
from app.models import Challenge
from app.schemas import ChallengeCreate, ChallengeUpdate, ChallengeRead


class ChallengeCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_challenge(self, id: int) -> Optional[ChallengeRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Challenge).where(Challenge.id == id))
            challenge: Optional[Challenge] = result.scalar()
            return ChallengeRead.model_validate(challenge) if challenge else None

    async def get_challenges(self, skip: int = 0, limit: int = 999) -> Optional[List[ChallengeRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(Challenge).offset(skip).limit(limit))
            challenges: Optional[List[Challenge]] = result.scalars().all()
            return [ChallengeRead.model_validate(challenge) for challenge in challenges] if challenges else None

    async def create_challenge(self, challenge: ChallengeCreate) -> Challenge:
        async with self.insert_session_scope() as s:
            db_challenge = Challenge(**challenge.dict())
            s.add(db_challenge)
            await s.flush()
            return db_challenge

    async def update_challenge(self, challenge: ChallengeUpdate) -> Optional[ChallengeRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(Challenge)
                .where(Challenge.id == challenge.id)
                .values(**challenge.dict(exclude_unset=True))
                .returning(Challenge)
            )
            challenge: Optional[Challenge] = result.scalar()
            return ChallengeRead.model_validate(challenge) if challenge else None

    async def delete_challenge(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(
                delete(Challenge)
                .where(Challenge.id == id)
            )
