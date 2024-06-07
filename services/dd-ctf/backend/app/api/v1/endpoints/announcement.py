from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import announcement_crud
from app.schemas import AnnouncementCreate, AnnouncementUpdate, AnnouncementRead

router = APIRouter()


@router.post("/", response_model=AnnouncementRead)
async def create_announcement(announcement: AnnouncementCreate):
    return await announcement_crud.create_announcement(announcement)


@router.get("/{announcement_id}", response_model=AnnouncementRead)
async def get_announcement(announcement_id: int):
    announcement = await announcement_crud.get_announcement(announcement_id)
    if announcement is None:
        raise HTTPException(status_code=404, detail="Announcement not found")
    return announcement


@router.get("/", response_model=List[AnnouncementRead])
async def get_announcements(skip: int = 0, limit: int = 100):
    return await announcement_crud.get_announcements(skip, limit)


@router.put("/{announcement_id}", response_model=AnnouncementRead)
async def update_announcement(announcement: AnnouncementUpdate):
    updated_announcement = await announcement_crud.update_announcement(announcement)
    if updated_announcement is None:
        raise HTTPException(status_code=404, detail="Announcement not found")
    return updated_announcement


@router.delete("/{announcement_id}", response_model=AnnouncementRead)
async def delete_announcement(announcement_id: int):
    deleted_announcement = await announcement_crud.delete_announcement(announcement_id)
    if deleted_announcement is None:
        raise HTTPException(status_code=404, detail="Announcement not found")
    return deleted_announcement
