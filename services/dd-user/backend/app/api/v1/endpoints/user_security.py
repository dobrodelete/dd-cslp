from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import user_security_crud
from app.schemas import UserSecurityCreate, UserSecurityRead

router = APIRouter()


@router.post("/", response_model=UserSecurityRead)
async def create_user_security(user_security: UserSecurityCreate):
    return await user_security_crud.create_user_security(user_security)


@router.get("/{user_security_id}", response_model=UserSecurityRead)
async def get_user_security(user_security_id: int):
    user_security = await user_security_crud.get_user_security(user_security_id)
    if user_security is None:
        raise HTTPException(status_code=404, detail="User security not found")
    return user_security


@router.get("/", response_model=List[UserSecurityRead])
async def get_user_securities(skip: int = 0, limit: int = 100):
    return await user_security_crud.get_user_securities(skip, limit)
