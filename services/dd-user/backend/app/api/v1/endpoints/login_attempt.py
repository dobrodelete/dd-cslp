from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import login_attempt_crud
from app.schemas import LoginAttemptCreate, LoginAttemptRead, LoginAttemptUpdate

router = APIRouter()


@router.get("/{id}", response_model=LoginAttemptRead)
async def get_login_attempt(id: int):
    login_attempt = await login_attempt_crud.get_login_attempt(id)
    if not login_attempt:
        raise HTTPException(status_code=404, detail="Login attempt not found")
    return login_attempt


@router.get("/", response_model=List[LoginAttemptRead])
async def get_login_attempts(skip: int = 0, limit: int = 100):
    return await login_attempt_crud.get_login_attempts(skip, limit)


@router.post("/", response_model=LoginAttemptRead)
async def create_login_attempt(login_attempt: LoginAttemptCreate):
    return await login_attempt_crud.create_login_attempt(login_attempt)


@router.put("/{id}", response_model=LoginAttemptRead)
async def update_login_attempt(id: int, login_attempt: LoginAttemptUpdate):
    existing_login_attempt = await login_attempt_crud.get_login_attempt(id)
    if not existing_login_attempt:
        raise HTTPException(status_code=404, detail="Login attempt not found")
    return await login_attempt_crud.update_login_attempt(login_attempt)


@router.delete("/{id}", response_model=None)
async def delete_login_attempt(id: int):
    existing_login_attempt = await login_attempt_crud.get_login_attempt(id)
    if not existing_login_attempt:
        raise HTTPException(status_code=404, detail="Login attempt not found")
    await login_attempt_crud.delete_login_attempt(id)
