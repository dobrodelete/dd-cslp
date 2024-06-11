from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import user_security_crud
from app.schemas import UserSecurityCreate, UserSecurityRead, UserSecurityUpdate

router = APIRouter()


@router.get("/", response_model=List[UserSecurityRead])
async def get_user_securities(skip: int = 0, limit: int = 100):
    return await user_security_crud.get_user_securities(skip=skip, limit=limit)


@router.get("/{id}", response_model=UserSecurityRead)
async def get_user_security(id: int):
    user_security = await user_security_crud.get_user_security(id)
    if user_security is None:
        raise HTTPException(status_code=404, detail="User security not found")
    return user_security


@router.post("/", response_model=UserSecurityRead)
async def create_user_security(user_security: UserSecurityCreate):
    return await user_security_crud.create_user_security(user_security)


@router.put("/{id}", response_model=UserSecurityRead)
async def update_user_security(id: int, user_security: UserSecurityUpdate):
    updated_user_security = await user_security_crud.update_user_security(user_security)
    if updated_user_security is None:
        raise HTTPException(status_code=404, detail="User security not found")
    return updated_user_security


@router.delete("/{id}", response_model=UserSecurityRead)
async def delete_user_security(id: int):
    deleted_user_security = await user_security_crud.delete_user_security(id)
    if deleted_user_security is None:
        raise HTTPException(status_code=404, detail="User security not found")
    return deleted_user_security
