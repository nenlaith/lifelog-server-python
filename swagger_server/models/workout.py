from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import ENUM

from swagger_server.models import Period


class Workout(Period):
    __mapper_args__ = {
        'polymorphic_identity': __tablename__,
        'column_prefix': __tablename__ + '_'
    }

    type = Column(ENUM('cardio', 'hiit_legs', 'hiit_arms', 'hiit_abs', 'yoga'), nullable=False)
