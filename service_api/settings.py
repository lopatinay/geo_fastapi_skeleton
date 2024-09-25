from uuid import uuid4
from pathlib import PosixPath, Path

from pydantic_settings import BaseSettings

from service_api.constants import AppEnvs


class Settings(BaseSettings):
    class Config:
        env_file = ".env"

    # App
    app_runtime_id: str = uuid4().hex
    app_env: str = AppEnvs.localhost
    debug: bool = True
    base_dir: PosixPath = Path(__file__).resolve().parent.parent
    log_level: str = "DEBUG"

    # Databases
    pg_dsn: str = "postgresql+psycopg://skeleton:skeleton@localhost:5432/skeleton"
    pg_test_dsn: str = "postgresql+psycopg://skeleton:skeleton@localhost:5432/skeleton_test"
    pg_echo: bool = True


RuntimeSettings = Settings()
