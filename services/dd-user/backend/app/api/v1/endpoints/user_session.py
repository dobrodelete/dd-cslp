from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import user_session_crud
from app.schemas import UserSessionCreate, UserSessionRead, UserSessionUpdate

router = APIRouter()


@router.get("/", response_model=List[UserSessionRead])
async def get_user_sessions(skip: int = 0, limit: int = 100):
    return await user_session_crud.get_user_sessions(skip=skip, limit=limit)


@router.get("/{id}", response_model=UserSessionRead)
async def get_user_session(id: int):
    user_session = await user_session_crud.get_user_session(id)
    if user_session is None:
        raise HTTPException(status_code=404, detail="User session not found")
    return user_session


@router.post("/", response_model=UserSessionRead)
async def create_user_session(user_session: UserSessionCreate):
    return await user_session_crud.create_user_session(user_session)


@router.put("/{id}", response_model=UserSessionRead)
async def update_user_session(id: int, user_session: UserSessionUpdate):
    updated_user_session = await user_session_crud.update_user_session(user_session)
    if updated_user_session is None:
        raise HTTPException(status_code=404, detail="User session not found")
    return updated_user_session


@router.delete("/{id}", response_model=UserSessionRead)
async def delete_user_session(id: int):
    deleted_user_session = await user_session_crud.delete_user_session(id)
    if deleted_user_session is None:
        raise HTTPException(status_code=404, detail="User session not found")
    return deleted_user_session
