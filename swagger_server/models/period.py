from sqlalchemy import Column, ColumnDefault
from sqlalchemy.dialects.postgresql import TSTZRANGE, VARCHAR, TEXT

from swagger_server.models.element_base import ElementBase


class Period(ElementBase):
    __tablename__ = 'period'
    __mapper_args__ = {
        'column_prefix': 'period_',
        'polymorphic_on': 'period_type'
    }

    range = Column(TSTZRANGE, nullable=False)
    type = Column(VARCHAR, nullable=False)
    description = Column(TEXT, ColumnDefault(''))
