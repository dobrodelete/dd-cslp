from .base import CrudBase
from .association import AssociationCrud
from .blocked_ip import BlockedIPCrud
from .login_attempt import LoginAttemptCrud
from .password_change import PasswordChangeCrud
from .permission import PermissionCrud
from .role import RoleCrud
from .user import UserCrud
from .user_access_log import UserAccessLogCrud
from .user_security import UserSecurityCrud
from .user_session import UserSessionCrud
from .user_settings import UserSettingsCrud

association_crud = AssociationCrud()
blocked_ip_crud = BlockedIPCrud()
login_attempt_crud = LoginAttemptCrud()
password_change_crud = PasswordChangeCrud()
permission_crud = PermissionCrud()
role_crud = RoleCrud()
user_crud = UserCrud()
user_access_log_crud = UserAccessLogCrud()
user_security_crud = UserSecurityCrud()
user_session_crud = UserSessionCrud()
user_settings_crud = UserSettingsCrud()

__all__ = [attr for attr in locals().keys() if not attr.startswith("_")]

