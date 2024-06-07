from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import user_session_crud
from app.schemas import UserSessionCreate, UserSessionRead

router = APIRouter()


@router.post("/", response_model=UserSessionRead)
async def create_user_session(user_session: UserSessionCreate):
    return await user_session_crud.create_user_session(user_session)


@router.get("/{user_session_id}", response_model=UserSessionRead)
async def get_user_session(user_session_id: int):
    user_session = await user_session_crud.get_user_session(user_session_id)
    if user_session is None:
        raise HTTPException(status_code=404, detail="User session not found")
    return user_session


@router.get("/", response_model=List[UserSessionRead])
async def get_user_sessions(skip: int = 0, limit: int = 100):
    return await user_session_crud.get_user_sessions(skip, limit)
