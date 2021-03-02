from sqlalchemy import Column, CheckConstraint
from sqlalchemy.dialects.postgresql import TEXT, INTEGER

from swagger_server.models import DayDescriptor


class Mood(DayDescriptor):
    __mapper_args__ = {
        'polymorphic_identity': __tablename__,
        'column_prefix': __tablename__ + '_'
    }
    description = Column(TEXT, nullable=False)
    anxiousness = Column(INTEGER, CheckConstraint('mood_anxiousness >= 0 and mood_anxiousness <= 10'), nullable=False)
    depress = Column(INTEGER, CheckConstraint('mood_depress >= 0 and mood_depress <= 10'), nullable=False)
