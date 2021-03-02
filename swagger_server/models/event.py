from sqlalchemy import Column, ColumnDefault
from sqlalchemy.dialects.postgresql import VARCHAR, TIMESTAMP

from swagger_server.models.element_base import ElementBase
import datetime


class Event(ElementBase):
    __mapper_args__ = {
        'polymorphic_on': __tablename__ + '_type',
        'column_prefix': __tablename__ + '_'
    }

    timestamp = Column(TIMESTAMP, ColumnDefault(datetime.datetime.now))
    type = Column(VARCHAR, nullable=False)
