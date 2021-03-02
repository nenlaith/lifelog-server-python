from sqlalchemy import Column, CheckConstraint
from sqlalchemy.dialects.postgresql import FLOAT

from swagger_server.models import Event


class Weigh(Event):
    __mapper_args__ = {
        'polymorphic_identity': __tablename__,
        'column_prefix': __tablename__ + '_'
    }

    heaviness = Column(FLOAT, CheckConstraint("weigh_heaviness >= 0.0"), nullable=False)
