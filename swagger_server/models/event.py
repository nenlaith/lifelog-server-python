import datetime

from sqlalchemy import Column, ColumnDefault, ForeignKey
from sqlalchemy.dialects.postgresql import VARCHAR, TIMESTAMP, UUID

from swagger_server.models.element_base import ElementBase
from swagger_server.models.type_mixin import TypeMixin
from swagger_server.models.uuid_mixin import UUIDMixin


class Event(UUIDMixin, TypeMixin, ElementBase):
    timestamp = Column(TIMESTAMP, ColumnDefault(datetime.datetime.now))
    event_type = Column(VARCHAR, nullable=False)
