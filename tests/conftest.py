import pytest
from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database

from service_api.app import fast_app
from service_api.models import BaseModel
from service_api.services.postgresql import db_session
from service_api.settings import RuntimeSettings

test_fast_app = TestClient(fast_app)
pg_engine = create_async_engine(RuntimeSettings.pg_test_dsn)
db_session_maker = async_sessionmaker(pg_engine, expire_on_commit=False, autocommit=False, autoflush=False)


async def _test_db_session():
    async with db_session_maker() as session:
        yield session


fast_app.dependency_overrides[db_session] = _test_db_session


@pytest.fixture
async def test_db_session():
    async with db_session_maker() as session:
        yield session


@pytest.fixture
def api_client():
    return test_fast_app


@pytest.fixture(scope="session", autouse=True)
def create_test_database():
    engine = create_engine(RuntimeSettings.pg_test_dsn)
    if not database_exists(engine.url):
        create_database(engine.url)
    engine.dispose()

    alembic_cfg = Config(str(RuntimeSettings.base_dir / "alembic.ini"))
    alembic_cfg.set_main_option("script_location", str(RuntimeSettings.base_dir / "alembic"))
    alembic_cfg.set_main_option("sqlalchemy.url", RuntimeSettings.pg_test_dsn)
    command.upgrade(alembic_cfg, "head")

    yield

    drop_database(RuntimeSettings.pg_test_dsn)


@pytest.fixture(autouse=True)
def clear_database():
    engine = create_engine(RuntimeSettings.pg_test_dsn)
    db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    with db_session() as session:
        for table in reversed(BaseModel.metadata.sorted_tables):
            session.execute(text(f'TRUNCATE TABLE "{table.name}" CASCADE;'))
        session.commit()

    engine.dispose()

    yield
