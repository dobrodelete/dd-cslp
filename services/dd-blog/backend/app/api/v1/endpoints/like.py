from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import like_crud
from app.schemas import LikeCreate, LikeRead

router = APIRouter()


@router.post("/", response_model=LikeRead)
async def create_like(like: LikeCreate):
    return await like_crud.create_like(like)


@router.get("/{like_id}", response_model=LikeRead)
async def get_like(like_id: int):
    like = await like_crud.get_like(like_id)
    if like is None:
        raise HTTPException(status_code=404, detail="Like not found")
    return like


@router.get("/", response_model=List[LikeRead])
async def get_likes(skip: int = 0, limit: int = 100):
    return await like_crud.get_likes(skip, limit)


@router.delete("/{like_id}", response_model=LikeRead)
async def delete_like(like_id: int):
    deleted_like = await like_crud.delete_like(like_id)
    if deleted_like is None:
        raise HTTPException(status_code=404, detail="Like not found")
    return deleted_like
