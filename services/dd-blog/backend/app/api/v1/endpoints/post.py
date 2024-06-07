from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import post_crud
from app.schemas import PostCreate, PostUpdate, PostRead

router = APIRouter()


@router.post("/", response_model=PostRead)
async def create_post(post: PostCreate):
    return await post_crud.create_post(post)


@router.get("/{post_id}", response_model=PostRead)
async def get_post(post_id: int):
    post = await post_crud.get_post(post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.get("/", response_model=List[PostRead])
async def get_posts(skip: int = 0, limit: int = 100):
    return await post_crud.get_posts(skip, limit)


@router.put("/{post_id}", response_model=PostRead)
async def update_post(post: PostUpdate):
    updated_post = await post_crud.update_post(post)
    if updated_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post


@router.delete("/{post_id}", response_model=PostRead)
async def delete_post(post_id: int):
    deleted_post = await post_crud.delete_post(post_id)
    if deleted_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return deleted_post
