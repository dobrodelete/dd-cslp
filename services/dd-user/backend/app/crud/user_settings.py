from typing import Optional, List

from sqlalchemy import select, update, delete

from app.crud import CrudBase
from app.models import UserSettings
from app.schemas import UserSettingsCreate, UserSettingsUpdate, UserSettingsRead


class UserSettingsCrud(CrudBase):
    def __init__(self):
        super().__init__()

    async def get_user_setting(self, id: int) -> Optional[UserSettingsRead]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(UserSettings).where(UserSettings.id == id))
            user_setting: Optional[UserSettings] = result.scalar()
            return UserSettingsRead.model_validate(user_setting) if user_setting else None

    async def get_user_settings(self, skip: int = 0, limit: int = 999) -> Optional[List[UserSettingsRead]]:
        async with self.read_session_scope() as s:
            result = await s.execute(select(UserSettings).offset(skip).limit(limit))
            user_settings: Optional[List[UserSettings]] = result.scalars().all()
            return [UserSettingsRead.model_validate(user_setting) for user_setting in user_settings] if user_settings else None

    async def create_user_setting(self, user_setting: UserSettingsCreate) -> UserSettings:
        async with self.insert_session_scope() as s:
            db_user_setting = UserSettings(
                user_id=user_setting.user_id,
                setting_name=user_setting.setting_name,
                setting_value=user_setting.setting_value,
                last_updated=user_setting.last_updated,
            )
            s.add(db_user_setting)
            await s.flush()
            return db_user_setting

    async def update_user_setting(self, user_setting: UserSettingsUpdate) -> Optional[UserSettingsRead]:
        async with self.insert_session_scope() as s:
            result = await s.execute(
                update(UserSettings)
                .where(UserSettings.id == user_setting.id)
                .values(
                    user_id=user_setting.user_id,
                    setting_name=user_setting.setting_name,
                    setting_value=user_setting.setting_value,
                    last_updated=user_setting.last_updated,
                )
                .returning(UserSettings)
            )
            updated_user_setting: Optional[UserSettings] = result.scalar()
            return UserSettingsRead.model_validate(updated_user_setting) if updated_user_setting else None

    async def delete_user_setting(self, id: int) -> None:
        async with self.insert_session_scope() as s:
            await s.execute(delete(UserSettings).where(UserSettings.id == id))
