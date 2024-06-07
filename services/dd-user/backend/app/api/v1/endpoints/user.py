import uuid
from datetime import timedelta, datetime

from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer

from app.config import settings
from app.crud import user_crud, user_session_crud
from app.schemas import UserRead, Token, UserCreate, UserSessionCreate
from app.utils.jwt import encode_jwt, hash_password, create_access_token, create_refresh_token, create_jwt
from app.utils.validation import validate_auth_user, get_current_auth_user_for_refresh, \
    get_current_token_payload, get_current_active_auth_user

http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(
    prefix="/jwt",
    tags=["JWT"],
    dependencies=[Depends(http_bearer)],
)


@router.post("/register/", response_model=Token)
async def register(
        user: UserCreate,
        request: Request
):
    existing_user = await user_crud.get_user_by_username(user.username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )

    hashed_password = hash_password(user.password)
    user.password_hash = hashed_password

    created_user = await user_crud.create_user(user)

    user_agent = request.headers.get("user-agent")
    ip_address_v4 = request.client.host
    # ip_address_v6 = request.headers.get("x-forwarded-for", request.client.host)

    session_token = str(uuid.uuid4())
    access_token_expires = timedelta(minutes=settings.auth_jwt.access_token_expire_minutes)

    access_token = create_access_token(created_user)

    user_session = UserSessionCreate(
        user_id=created_user.id,
        session_token=access_token,
        expires_at=datetime.utcnow() + access_token_expires,
        ip_address=ip_address_v4,
        user_agent=user_agent
    )

    await user_session_crud.create_user_session(user_session)

    return Token(access_token=access_token, token_type="bearer")


@router.post("/login/", response_model=Token)
def auth_user_issue_jwt(
        user: UserRead = Depends(validate_auth_user),
):
    access_token = create_access_token(user)
    refresh_token = create_refresh_token(user)
    return Token(
        access_token=access_token,
        refresh_token=refresh_token,
    )


@router.post(
    "/refresh/",
    response_model=Token,
    response_model_exclude_none=True,
)
def auth_refresh_jwt(
        user: UserRead = Depends(get_current_auth_user_for_refresh),
):
    access_token = create_access_token(user)
    return Token(
        access_token=access_token,
    )


@router.post("/logout/")
async def auth_user_issue_jwt(
        user: UserRead = Depends(get_current_token_payload)
):
    ...


@router.get("/users/me/", response_model=UserRead)
async def auth_user_check_self_info(
        payload: dict = Depends(get_current_token_payload),
        user: UserRead = Depends(get_current_active_auth_user),
):
    # iat = payload.get("iat")
    return user
