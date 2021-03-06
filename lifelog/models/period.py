from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import TSTZRANGE, VARCHAR, TEXT

from lifelog.models.element_base import ElementBase
from lifelog.models.type_mixin import TypeMixin
from lifelog.models.uuid_mixin import UUIDMixin


class Period(UUIDMixin, TypeMixin, ElementBase):
    range = Column(TSTZRANGE, nullable=False)
    period_type = Column(VARCHAR, nullable=False)
    description = Column(TEXT, nullable=False)
