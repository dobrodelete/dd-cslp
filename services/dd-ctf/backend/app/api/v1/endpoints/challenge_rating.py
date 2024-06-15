from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import challenge_rating_crud
from app.schemas import ChallengeRatingCreate, ChallengeRatingRead, ChallengeRatingUpdate

router = APIRouter()


@router.post("/", response_model=ChallengeRatingRead)
async def create_rating(rating_in: ChallengeRatingCreate):
    rating = await challenge_rating_crud.create_rating(rating=rating_in)
    return rating


@router.get("/{rating_id}", response_model=ChallengeRatingRead)
async def get_rating(rating_id: int):
    rating = await challenge_rating_crud.get_rating(rating_id=rating_id)
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    return rating


@router.get("/", response_model=List[ChallengeRatingRead])
async def get_ratings(skip: int = 0, limit: int = 100):
    return await challenge_rating_crud.get_ratings(skip=skip, limit=limit)


@router.put("/{rating_id}", response_model=ChallengeRatingRead)
async def update_rating(rating_in: ChallengeRatingUpdate):
    rating = await challenge_rating_crud.update_rating(rating=rating_in)
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    return rating


@router.delete("/{rating_id}")
async def delete_rating(rating_id: int):
    await challenge_rating_crud.delete_rating(rating_id=rating_id)
    return {"message": "Rating deleted successfully"}
