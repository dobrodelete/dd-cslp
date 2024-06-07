from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import user_access_log_crud
from app.schemas import UserAccessLogCreate, UserAccessLogRead

router = APIRouter()


@router.post("/", response_model=UserAccessLogRead)
async def create_user_access_log(user_access_log: UserAccessLogCreate):
    return await user_access_log_crud.create_user_access_log(user_access_log)


@router.get("/{user_access_log_id}", response_model=UserAccessLogRead)
async def get_user_access_log(user_access_log_id: int):
    user_access_log = await user_access_log_crud.get_user_access_log(user_access_log_id)
    if user_access_log is None:
        raise HTTPException(status_code=404, detail="User access log not found")
    return user_access_log


@router.get("/", response_model=List[UserAccessLogRead])
async def get_user_access_logs(skip: int = 0, limit: int = 100):
    return await user_access_log_crud.get_user_access_logs(skip, limit)
