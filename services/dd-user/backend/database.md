classDiagram
direction BT
class alembic_version {
   varchar(32) version_num
}
class blocked_ips {
   varchar ip_address
   varchar block_reason
   timestamp blocked_at
   timestamp created_at
   bigint id
}
class login_attempts {
   bigint user_id
   timestamp attempt_time
   varchar ip_address_v4
   varchar ip_address_v6
   varchar user_agent
   boolean successful
   timestamp created_at
   bigint id
}
class password_changes {
   bigint user_id
   bytea old_password_hash
   bytea new_password_hash
   timestamp change_time
   timestamp created_at
   bigint id
}
class permissions {
   varchar name
   varchar description
   timestamp created_at
   bigint id
}
class role_permission_association {
   bigint role_id
   bigint permission_id
}
class roles {
   varchar name
   varchar description
   timestamp created_at
   bigint id
}
class user_access_log {
   bigint user_id
   timestamp timestamp
   varchar ip_address
   varchar action
   varchar status
   varchar user_agent
   varchar location
   timestamp created_at
   bigint id
}
class user_permission_association {
   bigint user_id
   bigint permission_id
}
class user_role_association {
   bigint user_id
   bigint role_id
}
class user_security {
   bigint user_id
   timestamp last_login
   integer login_attempts
   timestamp last_failed_login
   timestamp password_changed_at
   varchar password_reset_token
   timestamp password_reset_token_expires_at
   boolean account_lock
   timestamp account_lock_until
   timestamp created_at
   bigint id
}
class user_sessions {
   bigint user_id
   varchar session_token
   timestamp created_at
   timestamp expires_at
   varchar ip_address
   varchar user_agent
   bigint id
}
class user_settings {
   bigint user_id
   varchar setting_name
   varchar setting_value
   timestamp last_updated
   timestamp created_at
   bigint id
}
class users {
   varchar username
   bytea password_hash
   varchar email
   varchar phone_number
   varchar full_name
   boolean is_admin
   boolean is_active
   timestamp created_at
   timestamp updated_at
   bigint id
}

login_attempts  -->  users : user_id:id
password_changes  -->  users : user_id:id
role_permission_association  -->  permissions : permission_id:id
role_permission_association  -->  roles : role_id:id
user_access_log  -->  users : user_id:id
user_permission_association  -->  permissions : permission_id:id
user_permission_association  -->  users : user_id:id
user_role_association  -->  roles : role_id:id
user_role_association  -->  users : user_id:id
user_security  -->  users : user_id:id
user_sessions  -->  users : user_id:id
user_settings  -->  users : user_id:id
