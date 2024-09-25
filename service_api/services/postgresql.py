from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from service_api.constants import APP_NAME
from service_api.settings import RuntimeSettings


pg_engine = create_async_engine(
    RuntimeSettings.pg_dsn,
    echo_pool=RuntimeSettings.pg_echo,
    connect_args={
        "application_name": f"{APP_NAME}:{RuntimeSettings.app_runtime_id}"
    },
)

db_session_maker = async_sessionmaker(
    pg_engine, expire_on_commit=False, autocommit=False, autoflush=False
)


async def db_session():
    async with db_session_maker() as session:
        yield session
