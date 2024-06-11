from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import blocked_ip_crud
from app.schemas import BlockedIPCreate, BlockedIPRead, BlockedIPUpdate

router = APIRouter()


@router.get("/{id}", response_model=BlockedIPRead)
async def get_blocked_ip(id: int):
    blocked_ip = await blocked_ip_crud.get_blocked_ip(id)
    if not blocked_ip:
        raise HTTPException(status_code=404, detail="Blocked IP not found")
    return blocked_ip


@router.get("/ip_v4/{ip_address_v4}", response_model=BlockedIPRead)
async def get_blocked_ip_by_v4(ip_address_v4: str):
    blocked_ip = await blocked_ip_crud.get_blocked_ip_by_v4(ip_address_v4)
    if not blocked_ip:
        raise HTTPException(status_code=404, detail="Blocked IP not found")
    return blocked_ip


@router.get("/", response_model=List[BlockedIPRead])
async def get_blocked_ips(skip: int = 0, limit: int = 100):
    return await blocked_ip_crud.get_blocked_ips(skip, limit)


@router.post("/", response_model=BlockedIPRead)
async def create_blocked_ip(blocked_ip: BlockedIPCreate):
    return await blocked_ip_crud.create_blocked_ip(blocked_ip)


@router.put("/{id}", response_model=BlockedIPRead)
async def update_blocked_ip(id: int, blocked_ip: BlockedIPUpdate):
    existing_blocked_ip = await blocked_ip_crud.get_blocked_ip(id)
    if not existing_blocked_ip:
        raise HTTPException(status_code=404, detail="Blocked IP not found")
    return await blocked_ip_crud.update_blocked_ip(blocked_ip)


@router.delete("/{id}", response_model=None)
async def delete_blocked_ip(id: int):
    existing_blocked_ip = await blocked_ip_crud.get_blocked_ip(id)
    if not existing_blocked_ip:
        raise HTTPException(status_code=404, detail="Blocked IP not found")
    await blocked_ip_crud.delete_blocked_ip(id)
