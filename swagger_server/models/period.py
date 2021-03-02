from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import TSTZRANGE, VARCHAR, TEXT

from swagger_server.models.element_base import ElementBase


class Period(ElementBase):
    __mapper_args__ = {
        'polymorphic_on': __tablename__ + '_type',
        'column_prefix': __tablename__ + '_'
    }

    range = Column(TSTZRANGE, nullable=False)
    type = Column(VARCHAR, nullable=False)
    description = Column(TEXT, nullable=False)
