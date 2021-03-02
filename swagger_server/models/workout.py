from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import ENUM

from swagger_server.models.period import Period


class Workout(Period):
    workout_type = Column(ENUM('cardio', 'hiit_legs', 'hiit_arms', 'hiit_abs', 'yoga'), nullable=False)
