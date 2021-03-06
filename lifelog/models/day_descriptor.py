import datetime

from sqlalchemy import Column, ColumnDefault
from sqlalchemy.dialects.postgresql import VARCHAR, DATE

from lifelog.models.element_base import ElementBase
from lifelog.models.type_mixin import TypeMixin
from lifelog.models.uuid_mixin import UUIDMixin


class DayDescriptor(UUIDMixin, TypeMixin, ElementBase):
    date = Column(DATE, ColumnDefault(datetime.datetime.now), nullable=False)
    day_descriptor_type = Column(VARCHAR, nullable=False)
