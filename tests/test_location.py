from fastapi import status
from geoalchemy2.shape import to_shape
from service_api.domain.locations import create_location_uc
from service_api.schemas.location import LocationCreate


async def test_create_location(test_db_session, api_client):
    payload = {"name": "My Location", "geom": "POINT(30 10)"}
    resp = api_client.post("/api/v1/locations", json=payload)
    assert resp.status_code == status.HTTP_201_CREATED

    resp_data = resp.json()
    assert "POINT (30 10)" == resp_data["geom"]
    assert "My Location" == resp_data["name"]


async def test_get_location(test_db_session, api_client):
    db_loc = await create_location_uc(test_db_session, LocationCreate(name="test", geom="POINT(1 10)"))
    resp = api_client.get(f"/api/v1/locations/{db_loc.id}")
    assert resp.status_code == status.HTTP_200_OK

    resp_data = resp.json()
    assert db_loc.name == resp_data["name"]
    assert to_shape(db_loc.geom).wkt == resp_data["geom"]
    assert db_loc.id == resp_data["id"]
