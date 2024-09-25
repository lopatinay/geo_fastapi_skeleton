from geoalchemy2.shape import to_shape
from pydantic import BaseModel, field_validator


class LocationBase(BaseModel):
    name: str
    geom: str  # WKT


class LocationCreate(LocationBase):
    pass


class LocationRead(LocationBase):
    id: int

    # class Config:
    #     orm_mode = True
    @field_validator("geom", mode="before")
    def turn_geo_location_into_wkt(cls, value):
        return to_shape(value).wkt
