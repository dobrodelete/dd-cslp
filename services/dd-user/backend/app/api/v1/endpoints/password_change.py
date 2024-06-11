from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import password_change_crud
from app.schemas import PasswordChangeCreate, PasswordChangeRead, PasswordChangeUpdate

router = APIRouter()


@router.get("/{id}", response_model=PasswordChangeRead)
async def get_password_change(id: int):
    password_change = await password_change_crud.get_password_change(id)
    if not password_change:
        raise HTTPException(status_code=404, detail="Password change not found")
    return password_change


@router.get("/", response_model=List[PasswordChangeRead])
async def get_password_changes(skip: int = 0, limit: int = 100):
    return await password_change_crud.get_password_changes(skip, limit)


@router.post("/", response_model=PasswordChangeRead)
async def create_password_change(password_change: PasswordChangeCreate):
    return await password_change_crud.create_password_change(password_change)


@router.put("/{id}", response_model=PasswordChangeRead)
async def update_password_change(id: int, password_change: PasswordChangeUpdate):
    existing_password_change = await password_change_crud.get_password_change(id)
    if not existing_password_change:
        raise HTTPException(status_code=404, detail="Password change not found")
    return await password_change_crud.update_password_change(password_change)


@router.delete("/{id}", response_model=None)
async def delete_password_change(id: int):
    existing_password_change = await password_change_crud.get_password_change(id)
    if not existing_password_change:
        raise HTTPException(status_code=404, detail="Password change not found")
    await password_change_crud.delete_password_change(id)
