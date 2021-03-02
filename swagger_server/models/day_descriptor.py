import datetime

from sqlalchemy import Column, ColumnDefault
from sqlalchemy.dialects.postgresql import VARCHAR, DATE
from swagger_server.models.element_base import ElementBase


class DayDescriptor(ElementBase):
    __mapper_args__ = {
        'polymorphic_on': __tablename__ + '_type',
        'column_prefix': __tablename__ + '_'
    }

    date = Column(DATE, ColumnDefault(datetime.datetime.now))
    type = Column(VARCHAR, nullable=False)
