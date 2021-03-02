from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import TSTZRANGE, VARCHAR, TEXT

from swagger_server.models.element_base import ElementBase
from swagger_server.models.type_mixin import TypeMixin
from swagger_server.models.uuid_mixin import UUIDMixin


class Period(UUIDMixin, TypeMixin, ElementBase):
    range = Column(TSTZRANGE, nullable=False)
    period_type = Column(VARCHAR, nullable=False)
    description = Column(TEXT, nullable=False)
