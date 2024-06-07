from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import login_attempt_crud
from app.schemas import LoginAttemptCreate, LoginAttemptRead

router = APIRouter()


@router.post("/", response_model=LoginAttemptRead)
async def create_login_attempt(login_attempt: LoginAttemptCreate):
    return await login_attempt_crud.create_login_attempt(login_attempt)


@router.get("/{login_attempt_id}", response_model=LoginAttemptRead)
async def get_login_attempt(login_attempt_id: int):
    login_attempt = await login_attempt_crud.get_login_attempt(login_attempt_id)
    if login_attempt is None:
        raise HTTPException(status_code=404, detail="Login attempt not found")
    return login_attempt


@router.get("/", response_model=List[LoginAttemptRead])
async def get_login_attempts(skip: int = 0, limit: int = 100):
    return await login_attempt_crud.get_login_attempts(skip, limit)
