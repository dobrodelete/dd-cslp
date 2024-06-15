from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.crud import challenge_comment_crud
from app.schemas import ChallengeCommentCreate, ChallengeCommentRead, ChallengeCommentUpdate

router = APIRouter()


@router.post("/", response_model=ChallengeCommentRead)
async def create_comment(comment_in: ChallengeCommentCreate):
    comment = await challenge_comment_crud.create_comment(comment=comment_in)
    return comment


@router.get("/{comment_id}", response_model=ChallengeCommentRead)
async def get_comment(comment_id: int):
    comment = await challenge_comment_crud.get_comment(comment_id=comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment


@router.get("/", response_model=List[ChallengeCommentRead])
async def get_comments(skip: int = 0, limit: int = 100):
    return await challenge_comment_crud.get_comments(skip=skip, limit=limit)


@router.put("/{comment_id}", response_model=ChallengeCommentRead)
async def update_comment(comment_in: ChallengeCommentUpdate):
    comment = await challenge_comment_crud.update_comment(comment=comment_in)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment


@router.delete("/{comment_id}")
async def delete_comment(comment_id: int):
    await challenge_comment_crud.delete_comment(comment_id=comment_id)
    return {"message": "Comment deleted successfully"}
