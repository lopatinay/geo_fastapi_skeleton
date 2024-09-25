from service_api.models import LocationModel
from service_api.schemas.location import LocationCreate


async def create_location_uc(session, loc: LocationCreate) -> LocationModel:
    loc = LocationModel(name=loc.name, geom=loc.geom)
    session.add(loc)
    await session.commit()
    await session.refresh(loc)
    return loc


async def get_location_ud(session, loc_id) -> LocationModel:
    loc = await session.get(LocationModel, loc_id)
    return loc


async def update_location_uc(session, location):
    location.name = location.name
    location.geom = location.geom
    session.add(location)
    await session.commit()
    await session.refresh(location)
    return location


async def delete_location_uc(session, location_id):
    loc = await session.get(LocationModel, location_id)
    await session.delete(loc)
    await session.commit()
