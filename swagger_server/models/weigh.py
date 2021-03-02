from sqlalchemy import Column, CheckConstraint
from sqlalchemy.dialects.postgresql import FLOAT

from swagger_server.models.event import Event


class Weigh(Event):
    heaviness = Column(FLOAT, CheckConstraint("weigh_heaviness >= 0.0"), nullable=False)
