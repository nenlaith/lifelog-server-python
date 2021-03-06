from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import ENUM

from lifelog.models.consumable_mixin import ConsumableMixin
from lifelog.models.event import Event


class Drink(Event, ConsumableMixin):
    drink_type = Column(ENUM('coffee', 'tea', 'water', 'lemon_water', name="drink_type"), nullable=False)
