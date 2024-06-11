from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import permission_crud
from app.schemas import PermissionCreate, PermissionUpdate, PermissionRead, PermissionRoleRead

router = APIRouter()


@router.post("/", response_model=PermissionRead)
async def create_permission(permission: PermissionCreate):
    return await permission_crud.create_permission(permission)


@router.get("/{permission_id}", response_model=PermissionRead)
async def get_permission(permission_id: int):
    permission = await permission_crud.get_permission(permission_id)
    if permission is None:
        raise HTTPException(status_code=404, detail="Permission not found")
    return permission


@router.get("/", response_model=List[PermissionRead])
async def get_permissions(skip: int = 0, limit: int = 100):
    return await permission_crud.get_permissions(skip, limit)


@router.put("/{permission_id}", response_model=PermissionRead)
async def update_permission(permission: PermissionUpdate):
    updated_permission = await permission_crud.update_permission(permission)
    if updated_permission is None:
        raise HTTPException(status_code=404, detail="Permission not found")
    return updated_permission


@router.delete("/{permission_id}", response_model=PermissionRead)
async def delete_permission(permission_id: int):
    deleted_permission = await permission_crud.delete_permission(permission_id)
    if deleted_permission is None:
        raise HTTPException(status_code=404, detail="Permission not found")
    return deleted_permission


@router.get("/{permission_id}/roles", response_model=PermissionRoleRead)
async def get_permission_with_roles(permission_id: int):
    permission = await permission_crud.get_permission_with_roles(permission_id)
    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found")
    return permission


@router.get("/", response_model=List[PermissionRoleRead])
async def get_permissions_with_roles(skip: int = 0, limit: int = 100):
    return await permission_crud.get_permissions_with_roles(skip, limit)
