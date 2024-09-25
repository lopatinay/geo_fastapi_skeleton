from fastapi import APIRouter, Depends
from sqlalchemy import text

from service_api.services.logger import app_logger
from service_api.services.postgresql import db_session

system_resource = APIRouter()


@system_resource.get("/health", tags=["System"])
async def healthcheck(db_session=Depends(db_session)):
    try:
        await db_session.execute(text("select 1"))
        postgres_status = True
    except Exception as e:
        app_logger.error(e)
        postgres_status = False

    return {
        "postgres_status": postgres_status
    }
