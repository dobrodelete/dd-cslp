from typing import List
from fastapi import APIRouter, HTTPException
from app.crud import team_crud
from app.schemas import TeamCreate, TeamUpdate, TeamRead

router = APIRouter()


@router.post("/", response_model=TeamRead)
async def create_team(team: TeamCreate):
    return await team_crud.create_team(team)


@router.get("/{team_id}", response_model=TeamRead)
async def get_team(team_id: int):
    team = await team_crud.get_team(team_id)
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return team


@router.get("/", response_model=List[TeamRead])
async def get_teams(skip: int = 0, limit: int = 100):
    return await team_crud.get_teams(skip, limit)


@router.put("/{team_id}", response_model=TeamRead)
async def update_team(team: TeamUpdate):
    updated_team = await team_crud.update_team(team)
    if updated_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return updated_team


@router.delete("/{team_id}", response_model=TeamRead)
async def delete_team(team_id: int):
    deleted_team = await team_crud.delete_team(team_id)
    if deleted_team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return deleted_team
