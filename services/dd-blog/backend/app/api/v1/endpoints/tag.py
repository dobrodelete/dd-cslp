from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import tag_crud
from app.schemas import TagCreate, TagUpdate, TagRead

router = APIRouter()


@router.post("/", response_model=TagRead)
async def create_tag(tag: TagCreate):
    return await tag_crud.create_tag(tag)


@router.get("/{tag_id}", response_model=TagRead)
async def get_tag(tag_id: int):
    tag = await tag_crud.get_tag(tag_id)
    if tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag


@router.get("/", response_model=List[TagRead])
async def get_tags(skip: int = 0, limit: int = 100):
    return await tag_crud.get_tags(skip, limit)


@router.put("/{tag_id}", response_model=TagRead)
async def update_tag(tag: TagUpdate):
    updated_tag = await tag_crud.update_tag(tag)
    if updated_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return updated_tag


@router.delete("/{tag_id}", response_model=TagRead)
async def delete_tag(tag_id: int):
    deleted_tag = await tag_crud.delete_tag(tag_id)
    if deleted_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return deleted_tag
