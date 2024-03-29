from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import VARCHAR

from lifelog.models.event import Event


class Pill(Event):
    pill_type = Column(VARCHAR, nullable=False)
    name = Column(VARCHAR, nullable=False)
