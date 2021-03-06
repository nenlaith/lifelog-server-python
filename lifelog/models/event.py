import datetime

from sqlalchemy import Column, ColumnDefault
from sqlalchemy.dialects.postgresql import VARCHAR, TIMESTAMP

from lifelog.models.element_base import ElementBase
from lifelog.models.type_mixin import TypeMixin
from lifelog.models.uuid_mixin import UUIDMixin


class Event(UUIDMixin, TypeMixin, ElementBase):
    timestamp = Column(TIMESTAMP, ColumnDefault(datetime.datetime.now), nullable=False)
    event_type = Column(VARCHAR, nullable=False)
