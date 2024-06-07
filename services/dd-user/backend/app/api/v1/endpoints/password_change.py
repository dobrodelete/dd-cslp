from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import password_change_crud
from app.schemas import PasswordChangeCreate, PasswordChangeRead

router = APIRouter()


@router.post("/", response_model=PasswordChangeRead)
async def create_password_change(password_change: PasswordChangeCreate):
    return await password_change_crud.create_password_change(password_change)


@router.get("/{password_change_id}", response_model=PasswordChangeRead)
async def get_password_change(password_change_id: int):
    password_change = await password_change_crud.get_password_change(password_change_id)
    if password_change is None:
        raise HTTPException(status_code=404, detail="Password change not found")
    return password_change


@router.get("/", response_model=List[PasswordChangeRead])
async def get_password_changes(skip: int = 0, limit: int = 100):
    return await password_change_crud.get_password_changes(skip, limit)
