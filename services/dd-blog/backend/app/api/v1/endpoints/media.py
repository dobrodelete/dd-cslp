from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import media_crud
from app.schemas import MediaCreate, MediaUpdate, MediaRead

router = APIRouter()


@router.post("/", response_model=MediaRead)
async def create_media(media: MediaCreate):
    return await media_crud.create_media(media)


@router.get("/{media_id}", response_model=MediaRead)
async def get_media(media_id: int):
    media = await media_crud.get_media(media_id)
    if media is None:
        raise HTTPException(status_code=404, detail="Media not found")
    return media


@router.get("/", response_model=List[MediaRead])
async def get_medias(skip: int = 0, limit: int = 100):
    return await media_crud.get_medias(skip, limit)


@router.put("/{media_id}", response_model=MediaRead)
async def update_media(media: MediaUpdate):
    updated_media = await media_crud.update_media(media)
    if updated_media is None:
        raise HTTPException(status_code=404, detail="Media not found")
    return updated_media


@router.delete("/{media_id}", response_model=MediaRead)
async def delete_media(media_id: int):
    deleted_media = await media_crud.delete_media(media_id)
    if deleted_media is None:
        raise HTTPException(status_code=404, detail="Media not found")
    return deleted_media
