from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.orm import relationship

from lifelog.models.event import Event


class Meal(Event):
    description = Column(TEXT, nullable=False)

    ingredients = relationship("MealIngredient")
