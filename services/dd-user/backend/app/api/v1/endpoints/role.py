from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import role_crud
from app.schemas import RoleCreate, RoleUpdate, RoleRead

router = APIRouter()


@router.post("/", response_model=RoleRead)
async def create_role(role: RoleCreate):
    return await role_crud.create_role(role)


@router.get("/{role_id}", response_model=RoleRead)
async def get_role(role_id: int):
    role = await role_crud.get_role(role_id)
    if role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return role


@router.get("/", response_model=List[RoleRead])
async def get_roles(skip: int = 0, limit: int = 100):
    return await role_crud.get_roles(skip, limit)


@router.put("/{role_id}", response_model=RoleRead)
async def update_role(role: RoleUpdate):
    updated_role = await role_crud.update_role(role)
    if updated_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return updated_role


@router.delete("/{role_id}", response_model=RoleRead)
async def delete_role(role_id: int):
    deleted_role = await role_crud.delete_role(role_id)
    if deleted_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return deleted_role
