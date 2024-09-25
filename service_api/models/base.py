import re

from sqlalchemy.orm import declared_attr, DeclarativeBase, Mapped, mapped_column


class BaseModel(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return re.sub(
            r"(?<!^)(?=[A-Z])", "_", cls.__name__.removesuffix("Model")
        ).lower()
