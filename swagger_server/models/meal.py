from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.orm import relationship

from swagger_server.models import Event


class Meal(Event):
    __mapper_args__ = {
        "polymorphic_identity": __tablename__,
        "column_prefix": __tablename__ + '_'
    }

    description = Column(TEXT, nullable=False)
    ingredients = relationship("MealIngredient")
