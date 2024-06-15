from typing import Optional, List

from sqlalchemy import select, update, delete

from app.crud import CrudBase
from app.models import ChallengeRating
from app.schemas import ChallengeRatingRead, ChallengeRatingCreate, ChallengeRatingUpdate


class ChallengeRatingCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_rating(self, id: int) -> Optional[ChallengeRatingRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(ChallengeRating).where(ChallengeRating.id == id))
            rating: Optional[ChallengeRating] = result.scalar()
            return ChallengeRatingRead.model_validate(rating) if rating else None

    async def get_ratings(self, skip: int = 0, limit: int = 999) -> Optional[List[ChallengeRatingRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(ChallengeRating).offset(skip).limit(limit))
            ratings: Optional[List[ChallengeRating]] = result.scalars().all()
            return [ChallengeRatingRead.model_validate(rating) for rating in ratings] if ratings else None

    async def create_rating(self, rating: ChallengeRatingCreate) -> ChallengeRating:
        async with self.insert_session_scope() as s:
            db_rating = ChallengeRating(
                challenge_id=rating.challenge_id,
                user_id=rating.user_id,
                rating=rating.rating,
            )
            s.add(db_rating)
            await s.flush()
            return db_rating

    async def update_rating(self, rating: ChallengeRatingUpdate) -> Optional[ChallengeRatingRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(ChallengeRating)
                .where(ChallengeRating.id == rating.id)
                .values(
                    challenge_id=rating.challenge_id,
                    user_id=rating.user_id,
                    rating=rating.rating,
                )
                .returning(ChallengeRating)
            )
            updated_rating: Optional[ChallengeRating] = result.scalar()
            return ChallengeRatingRead.model_validate(updated_rating) if updated_rating else None

    async def delete_rating(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(delete(ChallengeRating).where(ChallengeRating.id == id))
