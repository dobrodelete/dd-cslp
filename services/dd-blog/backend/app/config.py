import os
from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent

PG_DB_USERNAME = os.environ.get("PG_DB_USERNAME", "postgres")
PG_DB_SECRET = os.environ.get("PG_DB_SECRET", "postgres")
PG_DB_HOST = os.environ.get("PG_DB_HOST", "localhost")
PG_DB_PORT = os.environ.get("PG_DB_PORT", "5432")
PG_DB_NAME = os.environ.get("PG_DB_NAME", "cslp_blog")


class DbSettings(BaseSettings):
    url: str = f"postgresql+asyncpg://{PG_DB_USERNAME}:{PG_DB_SECRET}@{PG_DB_HOST}:{PG_DB_PORT}/{PG_DB_NAME}"
    echo: bool = True


class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1/blog"

    db: DbSettings = DbSettings()

    auth_jwt: AuthJWT = AuthJWT()


settings = Settings()
