from contextlib import asynccontextmanager
from sqlalchemy.exc import SQLAlchemyError
from app.db.db_helper import db_helper


class CrudBase:
    def __init__(self):
        self.session = db_helper.session_factory

    @asynccontextmanager
    async def insert_session_scope(self):
        async with self.session.begin() as s:
            try:
                yield s
                await s.commit()
            except SQLAlchemyError as e:
                print(e)
                await s.rollback()
                raise
            finally:
                await s.close()

    @asynccontextmanager
    async def read_session_scope(self):
        async with self.session.begin() as s:
            try:
                yield s
            except SQLAlchemyError as e:
                print(e)
                raise
            finally:
                await s.close()
