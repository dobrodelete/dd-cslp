from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import blocked_ip_crud
from app.schemas import BlockedIPCreate, BlockedIPRead

router = APIRouter()


@router.post("/", response_model=BlockedIPRead)
async def create_blocked_ip(blocked_ip: BlockedIPCreate):
    return await blocked_ip_crud.create_blocked_ip(blocked_ip)


@router.get("/{blocked_ip_id}", response_model=BlockedIPRead)
async def get_blocked_ip(blocked_ip_id: int):
    blocked_ip = await blocked_ip_crud.get_blocked_ip(blocked_ip_id)
    if blocked_ip is None:
        raise HTTPException(status_code=404, detail="Blocked IP not found")
    return blocked_ip


@router.get("/", response_model=List[BlockedIPRead])
async def get_blocked_ips(skip: int = 0, limit: int = 100):
    return await blocked_ip_crud.get_blocked_ips(skip, limit)


@router.delete("/{blocked_ip_id}", response_model=BlockedIPRead)
async def delete_blocked_ip(blocked_ip_id: int):
    deleted_blocked_ip = await blocked_ip_crud.delete_blocked_ip(blocked_ip_id)
    if deleted_blocked_ip is None:
        raise HTTPException(status_code=404, detail="Blocked IP not found")
    return deleted_blocked_ip
