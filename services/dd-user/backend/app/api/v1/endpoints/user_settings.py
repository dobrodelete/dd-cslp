from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import user_settings_crud
from app.schemas import UserSettingsCreate, UserSettingsRead

router = APIRouter()


@router.post("/", response_model=UserSettingsRead)
async def create_user_settings(user_settings: UserSettingsCreate):
    return await user_settings_crud.create_user_setting(user_settings)


@router.get("/{user_settings_id}", response_model=UserSettingsRead)
async def get_user_settings(user_settings_id: int):
    user_settings = await user_settings_crud.get_user_setting(user_settings_id)
    if user_settings is None:
        raise HTTPException(status_code=404, detail="User settings not found")
    return user_settings


@router.get("/", response_model=List[UserSettingsRead])
async def get_user_settings(skip: int = 0, limit: int = 100):
    return await user_settings_crud.get_user_settings(skip, limit)
