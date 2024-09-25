from fastapi import APIRouter

from service_api.resources.system import system_resource
from service_api.resources.v1.location import location_resources

api = APIRouter()
api.include_router(system_resource)
api_v1 = APIRouter(prefix="/api/v1")
api_v1.include_router(location_resources)
api.include_router(api_v1)
