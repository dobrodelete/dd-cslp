from .admin.users import router as admin_users_router
from .admin.roles import router as admin_roles_router
from .admin.permissions import router as admin_permissions_router
from .association import router as association_router
from .blocked_ip import router as blocked_ip_router
from .check import router as check_router
from .login_attempt import router as login_attempt_router
from .password_change import router as password_change_router
from .permission import router as permission_router
from .role import router as role_router
from .user import router as user_router
from .user_access_log import router as user_access_log_router
from .user_security import router as user_security_router
from .user_session import router as user_session_router
from .user_settings import router as user_settings_router

__all__ = [attr for attr in locals().keys() if not attr.startswith("_")]
