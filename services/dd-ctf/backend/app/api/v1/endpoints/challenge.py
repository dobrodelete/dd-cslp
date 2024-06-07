from typing import List
from fastapi import APIRouter, HTTPException
from app.crud import challenge_crud
from app.schemas import ChallengeCreate, ChallengeUpdate, ChallengeRead

router = APIRouter()


@router.post("/", response_model=ChallengeRead)
async def create_challenge(challenge: ChallengeCreate):
    return await challenge_crud.create_challenge(challenge)


@router.get("/{challenge_id}", response_model=ChallengeRead)
async def get_challenge(challenge_id: int):
    challenge = await challenge_crud.get_challenge(challenge_id)
    if challenge is None:
        raise HTTPException(status_code=404, detail="Challenge not found")
    return challenge


@router.get("/", response_model=List[ChallengeRead])
async def get_challenges(skip: int = 0, limit: int = 100):
    return await challenge_crud.get_challenges(skip, limit)


@router.put("/{challenge_id}", response_model=ChallengeRead)
async def update_challenge(challenge: ChallengeUpdate):
    updated_challenge = await challenge_crud.update_challenge(challenge)
    if updated_challenge is None:
        raise HTTPException(status_code=404, detail="Challenge not found")
    return updated_challenge


@router.delete("/{challenge_id}", response_model=ChallengeRead)
async def delete_challenge(challenge_id: int):
    deleted_challenge = await challenge_crud.delete_challenge(challenge_id)
    if deleted_challenge is None:
        raise HTTPException(status_code=404, detail="Challenge not found")
    return deleted_challenge
