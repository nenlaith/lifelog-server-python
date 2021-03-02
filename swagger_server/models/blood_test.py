from sqlalchemy import Column, CheckConstraint
from sqlalchemy.dialects.postgresql import FLOAT, ENUM

from swagger_server.models.event import Event


class BloodTest(Event):
    blood_test_level = Column(FLOAT, CheckConstraint("blood_test_level >= 0.0"), nullable=False)
    blood_test_type = Column(ENUM('ketonemia', 'blood_sugar'), nullable=False)
