from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from app.db.db_helper import db_helper


def get_db() -> async_sessionmaker[AsyncSession]:
    return db_helper.session_factory
