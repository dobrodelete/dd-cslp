from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import user_access_log_crud
from app.schemas import UserAccessLogCreate, UserAccessLogRead, UserAccessLogUpdate

router = APIRouter()


@router.get("/", response_model=List[UserAccessLogRead])
async def get_user_access_logs(skip: int = 0, limit: int = 100):
    return await user_access_log_crud.get_user_access_logs(skip=skip, limit=limit)


@router.get("/{id}", response_model=UserAccessLogRead)
async def get_user_access_log(id: int):
    user_access_log = await user_access_log_crud.get_user_access_log(id)
    if user_access_log is None:
        raise HTTPException(status_code=404, detail="User access log not found")
    return user_access_log


@router.post("/", response_model=UserAccessLogRead)
async def create_user_access_log(user_access_log: UserAccessLogCreate):
    return await user_access_log_crud.create_user_access_log(user_access_log)


@router.put("/{id}", response_model=UserAccessLogRead)
async def update_user_access_log(user_access_log: UserAccessLogUpdate):
    updated_user_access_log = await user_access_log_crud.update_user_access_log(user_access_log)
    if updated_user_access_log is None:
        raise HTTPException(status_code=404, detail="User access log not found")
    return updated_user_access_log


@router.delete("/{id}", response_model=UserAccessLogRead)
async def delete_user_access_log(id: int):
    deleted_user_access_log = await user_access_log_crud.delete_user_access_log(id)
    if deleted_user_access_log is None:
        raise HTTPException(status_code=404, detail="User access log not found")
    return deleted_user_access_log
