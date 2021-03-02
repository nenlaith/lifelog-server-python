from sqlalchemy import Column, CheckConstraint
from sqlalchemy.dialects.postgresql import FLOAT, ENUM

from swagger_server.models import Event


class BloodTest(Event):
    __mapper_args__ = {
        'polymorphic_identity': __tablename__,
        'column_prefix': __tablename__ + '_'
    }

    level = Column(FLOAT, CheckConstraint("blood_test_level >= 0.0"), nullable=False)
    type = Column(ENUM('ketonemia', 'blood_sugar'), nullable=False)
