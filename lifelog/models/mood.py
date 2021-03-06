from sqlalchemy import Column, CheckConstraint
from sqlalchemy.dialects.postgresql import TEXT, INTEGER

from lifelog.models.day_descriptor import DayDescriptor


class Mood(DayDescriptor):
    description = Column(TEXT, nullable=False)
    anxiousness = Column(INTEGER, CheckConstraint('anxiousness >= 0 and anxiousness <= 10'), nullable=False)
    depress = Column(INTEGER, CheckConstraint('depress >= 0 and depress <= 10'), nullable=False)
