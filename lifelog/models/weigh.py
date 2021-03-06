from sqlalchemy import Column, CheckConstraint
from sqlalchemy.dialects.postgresql import REAL

from lifelog.models.event import Event


class Weigh(Event):
    heaviness = Column(REAL, CheckConstraint("heaviness >= 0.0"), nullable=False)
