from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import ENUM

from swagger_server.models.consumable_mixin import ConsumableMixin
from swagger_server.models.event import Event


class Drink(Event, ConsumableMixin):
    drink_type = Column(ENUM('coffee', 'tea', 'water', 'lemon_water'), nullable=False)
