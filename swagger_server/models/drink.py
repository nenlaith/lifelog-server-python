from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import ENUM

from swagger_server.models import Event
from swagger_server.models.consumable_mixin import ConsumableMixin


class Drink(Event, ConsumableMixin):

    __mapper_args__ = {
        'polymorphic_identity': __tablename__,
        'column_prefix': __tablename__ + '_'
    }

    type = Column(ENUM('coffee', 'tea', 'water', 'lemon_water'), nullable=False)
