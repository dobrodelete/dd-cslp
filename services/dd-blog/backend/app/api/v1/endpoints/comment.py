from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import comment_crud
from app.schemas import CommentCreate, CommentUpdate, CommentRead

router = APIRouter()


@router.post("/", response_model=CommentRead)
async def create_comment(comment: CommentCreate):
    return await comment_crud.create_comment(comment)


@router.get("/{comment_id}", response_model=CommentRead)
async def get_comment(comment_id: int):
    comment = await comment_crud.get_comment(comment_id)
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment


@router.get("/", response_model=List[CommentRead])
async def get_comments(skip: int = 0, limit: int = 100):
    return await comment_crud.get_comments(skip, limit)


@router.put("/{comment_id}", response_model=CommentRead)
async def update_comment(comment: CommentUpdate):
    updated_comment = await comment_crud.update_comment(comment)
    if updated_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return updated_comment


@router.delete("/{comment_id}", response_model=CommentRead)
async def delete_comment(comment_id: int):
    deleted_comment = await comment_crud.delete_comment(comment_id)
    if deleted_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return deleted_comment
