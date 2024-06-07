from typing import List
from fastapi import APIRouter, HTTPException
from app.crud import team_member_crud
from app.schemas import TeamMemberCreate, TeamMemberUpdate, TeamMemberRead

router = APIRouter()


@router.post("/", response_model=TeamMemberRead)
async def create_team_member(team_member: TeamMemberCreate):
    return await team_member_crud.create_team_member(team_member)


@router.get("/{team_member_id}", response_model=TeamMemberRead)
async def get_team_member(team_member_id: int):
    team_member = await team_member_crud.get_team_member(team_member_id)
    if team_member is None:
        raise HTTPException(status_code=404, detail="Team member not found")
    return team_member


@router.get("/", response_model=List[TeamMemberRead])
async def get_team_members(skip: int = 0, limit: int = 100):
    return await team_member_crud.get_team_members(skip, limit)


@router.put("/{team_member_id}", response_model=TeamMemberRead)
async def update_team_member(team_member: TeamMemberUpdate):
    updated_team_member = await team_member_crud.update_team_member(team_member)
    if updated_team_member is None:
        raise HTTPException(status_code=404, detail="Team member not found")
    return updated_team_member


@router.delete("/{team_member_id}", response_model=TeamMemberRead)
async def delete_team_member(team_member_id: int):
    deleted_team_member = await team_member_crud.delete_team_member(team_member_id)
    if deleted_team_member is None:
        raise HTTPException(status_code=404, detail="Team member not found")
    return deleted_team_member
