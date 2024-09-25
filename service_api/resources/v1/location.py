from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from service_api.domain.locations import create_location_uc, get_location_ud, update_location_uc, delete_location_uc
from service_api.schemas.location import LocationRead, LocationCreate
from service_api.services.postgresql import db_session

location_resources = APIRouter(prefix="/locations", tags=["Locations"])


@location_resources.post("/", response_model=LocationRead, status_code=status.HTTP_201_CREATED)
async def create_location(location: LocationCreate, session: AsyncSession = Depends(db_session)):
    loc = await create_location_uc(session, location)
    return loc


@location_resources.get("/{location_id}", response_model=LocationRead)
async def read_location(location_id: int, session: AsyncSession = Depends(db_session)):
    if loc := await get_location_ud(session, location_id):
        return loc
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Location not found")


@location_resources.put("/{location_id}", response_model=LocationRead, status_code=status.HTTP_201_CREATED)
async def update_location(location_id: int, location: LocationCreate, session: AsyncSession = Depends(db_session)):
    # it can be simpler by intercepting the error from Postgres instead doing addition query
    if loc := await get_location_ud(session, location_id):
        return await update_location_uc(session, loc)
    raise HTTPException(status_code=404, detail="Location not found")


@location_resources.delete("/{location_id}")
async def delete_location(location_id: int, session: AsyncSession = Depends(db_session)):
    # it can be simpler by intercepting the error from Postgres instead doing addition query
    if await get_location_ud(session, location_id):
        return await delete_location_uc(session, location_id)
    return {"detail": "Location deleted"}
