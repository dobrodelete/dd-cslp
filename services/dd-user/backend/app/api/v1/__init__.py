from fastapi import APIRouter

from .endpoints import association_router, blocked_ip_router, login_attempt_router, password_change_router, \
    permission_router, role_router, user_router, user_access_log_router, user_security_router, user_session_router, \
    user_settings_router

api_router = APIRouter()

api_router.include_router(user_router)
api_router.include_router(association_router, prefix="/association", tags=["association"])
api_router.include_router(blocked_ip_router, prefix="/blocked_ip", tags=["blocked ip"])
api_router.include_router(login_attempt_router, prefix="/login_attempt", tags=["login attempt"])
api_router.include_router(password_change_router, prefix="/password_change", tags=["password change"])
api_router.include_router(permission_router, prefix="/permission", tags=["permission"])
api_router.include_router(role_router, prefix="/role", tags=["role"])
api_router.include_router(user_access_log_router, prefix="/user_access_log", tags=["user access log"])
api_router.include_router(user_security_router, prefix="/user_security", tags=["user security"])
api_router.include_router(user_session_router, prefix="/user_session", tags=["user session"])
api_router.include_router(user_settings_router, prefix="/user_settings", tags=["user settings"])
