from sqlalchemy import Column, ColumnDefault
from sqlalchemy.dialects.postgresql import VARCHAR, TIMESTAMP
from swagger_server.models.element_base import ElementBase
import datetime


class Event(ElementBase):
    __tablename__ = 'event'
    __mapper_args__ = {
        'column_prefix': 'event_',
        'polymorphic_on': 'event_type'
    }

    timestamp = Column(TIMESTAMP, ColumnDefault(datetime.datetime.now))
    type = Column(VARCHAR, nullable=False)
