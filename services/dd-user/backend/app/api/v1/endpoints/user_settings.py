from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import user_settings_crud
from app.schemas import UserSettingsCreate, UserSettingsRead, UserSettingsUpdate

router = APIRouter()


@router.get("/", response_model=List[UserSettingsRead])
async def get_user_settings(skip: int = 0, limit: int = 100):
    return await user_settings_crud.get_user_settings(skip=skip, limit=limit)


@router.get("/{id}", response_model=UserSettingsRead)
async def get_user_setting(id: int):
    user_setting = await user_settings_crud.get_user_setting(id)
    if user_setting is None:
        raise HTTPException(status_code=404, detail="User setting not found")
    return user_setting


@router.post("/", response_model=UserSettingsRead)
async def create_user_setting(user_setting: UserSettingsCreate):
    return await user_settings_crud.create_user_setting(user_setting)


@router.put("/{id}", response_model=UserSettingsRead)
async def update_user_setting(id: int, user_setting: UserSettingsUpdate):
    updated_user_setting = await user_settings_crud.update_user_setting(user_setting)
    if updated_user_setting is None:
        raise HTTPException(status_code=404, detail="User setting not found")
    return updated_user_setting


@router.delete("/{id}", response_model=UserSettingsRead)
async def delete_user_setting(id: int):
    deleted_user_setting = await user_settings_crud.delete_user_setting(id)
    if deleted_user_setting is None:
        raise HTTPException(status_code=404, detail="User setting not found")
    return deleted_user_setting
