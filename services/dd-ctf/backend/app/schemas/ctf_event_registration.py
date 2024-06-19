from datetime import datetime

from pydantic import ConfigDict, BaseModel


class CTFEventRegistrationBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    event_id: int
    registered_at: datetime


class CTFEventRegistrationCreate(CTFEventRegistrationBase):
    pass


class CTFEventRegistrationRead(CTFEventRegistrationBase):
    id: int
    created_at: datetime
    updated_at: datetime


class CTFEventRegistrationUpdate(CTFEventRegistrationBase):
    id: int
