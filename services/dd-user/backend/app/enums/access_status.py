from enum import StrEnum


class AccessStatus(StrEnum):
    SUCCESS = "success"
    FAILED = "failed"
    LOCKED_OUT = "locked_out"
    PASSWORD_RESET = "password_reset"
    USER_CREATED = "user_created"
    USER_DELETED = "user_deleted"
