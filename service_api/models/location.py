from service_api.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from geoalchemy2 import Geometry, WKBElement


class LocationModel(BaseModel):
    name: Mapped[str] = mapped_column(index=True)
    geom: Mapped[WKBElement] = mapped_column(Geometry(geometry_type='POINT', srid=4326))
