import httpx
from fastapi import APIRouter, HTTPException

router = APIRouter()

USER_SERVICE_URL = "http://user-service:8000"


@router.post("/login/")
async def login(data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{USER_SERVICE_URL}/jwt/login", json=data)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error during login")
        return response.json()


@router.post("/register/")
async def register(data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{USER_SERVICE_URL}/jwt/register", json=data)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Error during registration")
        return response.json()
