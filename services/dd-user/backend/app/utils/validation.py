from typing import Annotated

from fastapi import Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext

from app.crud import user_crud
from app.schemas import UserRead, LoginRequest
from app.utils.jwt import decode_jwt, validate_password, TOKEN_TYPE_FIELD, ACCESS_TOKEN_TYPE, REFRESH_TOKEN_TYPE

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/jwt/login")


def get_current_token_payload(
        token: str = Depends(oauth2_scheme),
) -> dict:
    try:
        payload = decode_jwt(
            token=token,
        )
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token error: {e}",
        )
    return payload


def validate_token_type(
        payload: dict,
        token_type: str,
) -> bool:
    current_token_type = payload.get(TOKEN_TYPE_FIELD)
    if current_token_type == token_type:
        return True
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"invalid token type {current_token_type!r} expected {token_type!r}",
    )


async def get_user_by_token_sub(payload: dict) -> UserRead:
    username: str | None = payload.get("sub")
    if user := await user_crud.get_user_by_username(username):
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token invalid (user not found)",
    )


def get_auth_user_from_token_of_type(token_type: str):
    async def get_auth_user_from_token(
            payload: dict = Depends(get_current_token_payload),
    ) -> UserRead:
        validate_token_type(payload, token_type)
        return await get_user_by_token_sub(payload)

    return get_auth_user_from_token


class UserGetterFromToken:
    def __init__(self, token_type: str):
        self.token_type = token_type

    def __call__(
            self,
            payload: dict = Depends(get_current_token_payload),
    ):
        validate_token_type(payload, self.token_type)
        return get_user_by_token_sub(payload)


get_current_auth_user = get_auth_user_from_token_of_type(ACCESS_TOKEN_TYPE)

get_current_auth_user_for_refresh = UserGetterFromToken(REFRESH_TOKEN_TYPE)


def get_current_active_auth_user(
        user: UserRead = Depends(get_current_auth_user),
):
    if user.is_active:
        return user
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="inactive user",
    )


async def validate_auth_user(
        login_request: LoginRequest
):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
    )
    user = await user_crud.get_user_by_username(login_request.username)
    if not user:
        raise unauthed_exc

    if not validate_password(
            password=login_request.password,
            hashed_password=user.password_hash,
    ):
        raise unauthed_exc

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User is inactive",
        )

    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_jwt(token)
        return payload
    except JWTError:
        raise credentials_exception


async def validate_user(
        username: Annotated[str, Form()],
        password: Annotated[str, Form()],
):
    unauthorized_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
    )
    user = await user_crud.get_user_by_username(username)
    if not user:
        raise unauthorized_exc

    if not validate_password(
            password=password,
            hashed_password=user.password_hash,
    ):
        raise unauthorized_exc

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User inactive",
        )
    return user


async def get_current_admin_user(current_user: UserRead = Depends(get_current_user)) -> UserRead:
    if not any(role.name == "admin" for role in current_user.roles):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to access this resource."
        )
    return current_user
