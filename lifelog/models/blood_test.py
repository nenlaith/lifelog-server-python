from sqlalchemy import Column, CheckConstraint
from sqlalchemy.dialects.postgresql import REAL, ENUM

from lifelog.models.event import Event


class BloodTest(Event):
    blood_test_level = Column(REAL, CheckConstraint("blood_test_level >= 0.0"), nullable=False)
    blood_test_type = Column(ENUM('ketonemia', 'blood_sugar', name="blood_test_type"), nullable=False)
