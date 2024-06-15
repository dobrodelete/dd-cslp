from typing import Optional, List

from sqlalchemy import select, update, delete

from app.crud import CrudBase
from app.models import File
from app.schemas import FileRead, FileCreate, FileUpdate


class FileCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_file(self, id: int) -> Optional[FileRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(File).where(File.id == id))
            file: Optional[File] = result.scalar()
            return FileRead.model_validate(file) if file else None

    async def get_files(self, skip: int = 0, limit: int = 999) -> Optional[List[FileRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(File).offset(skip).limit(limit))
            files: Optional[List[File]] = result.scalars().all()
            return [FileRead.model_validate(file) for file in files] if files else None

    async def create_file(self, file: FileCreate) -> File:
        async with self.insert_session_scope() as s:
            db_file = File(
                filename=file.filename,
                filepath=file.filepath,
                challenge_id=file.challenge_id,
                uploaded_at=file.uploaded_at,
            )
            s.add(db_file)
            await s.flush()
            return db_file

    async def update_file(self, file: FileUpdate) -> Optional[FileRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(File)
                .where(File.id == file.id)
                .values(
                    filename=file.filename,
                    filepath=file.filepath,
                    challenge_id=file.challenge_id,
                    uploaded_at=file.uploaded_at,
                )
                .returning(File)
            )
            updated_file: Optional[File] = result.scalar()
            return FileRead.model_validate(updated_file) if updated_file else None

    async def delete_file(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(delete(File).where(File.id == id))
