import datetime

from sqlalchemy import Column, ColumnDefault
from sqlalchemy.dialects.postgresql import VARCHAR, DATE

from swagger_server.models.element_base import ElementBase
from swagger_server.models.type_mixin import TypeMixin
from swagger_server.models.uuid_mixin import UUIDMixin


class DayDescriptor(UUIDMixin, TypeMixin, ElementBase):
    date = Column(DATE, ColumnDefault(datetime.datetime.now))
    day_descriptor_type = Column(VARCHAR, nullable=False)
