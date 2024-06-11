from datetime import timedelta, datetime

import jwt
from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session

from app.config import settings
from app.db.db_helper import db_helper

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM


def get_db() -> async_sessionmaker[AsyncSession]:
    return db_helper.session_factory


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
