from fastapi import APIRouter

from app.crud import association_crud

router = APIRouter()


@router.post("/add_role_permission")
async def add_role_permission(role_id: int, permission_id: int):
    await association_crud.add_role_permission(role_id, permission_id)
    return {"message": "Permission added to role"}


@router.delete("/remove_role_permission")
async def remove_role_permission(role_id: int, permission_id: int):
    await association_crud.remove_role_permission(role_id, permission_id)
    return {"message": "Permission removed from role"}


@router.post("/add_user_permission")
async def add_user_permission(user_id: int, permission_id: int):
    await association_crud.add_user_permission(user_id, permission_id)
    return {"message": "Permission added to user"}


@router.delete("/remove_user_permission")
async def remove_user_permission(user_id: int, permission_id: int):
    await association_crud.remove_user_permission(user_id, permission_id)
    return {"message": "Permission removed from user"}


@router.post("/add_user_role")
async def add_user_role(user_id: int, role_id: int):
    await association_crud.add_user_role(user_id, role_id)
    return {"message": "Role added to user"}


@router.delete("/remove_user_role")
async def remove_user_role(user_id: int, role_id: int):
    await association_crud.remove_user_role(user_id, role_id)
    return {"message": "Role removed from user"}
