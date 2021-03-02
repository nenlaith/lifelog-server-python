from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import VARCHAR

from swagger_server.models import Event


class Pill(Event):
    __mapper_args__ = {
        'polymorphic_identity': __tablename__,
        'column_prefix': __tablename__ + '_'
    }

    type = Column(VARCHAR, nullable=False)
    name = Column(VARCHAR, nullable=False)
