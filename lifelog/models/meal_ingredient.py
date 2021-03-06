from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import ENUM, VARCHAR, UUID
from sqlalchemy.orm import relationship

from lifelog.models.consumable_mixin import ConsumableMixin
from lifelog.models.element_base import ElementBase
from lifelog.models.uuid_mixin import UUIDMixin


class MealIngredient(UUIDMixin, ConsumableMixin, ElementBase):
    ingredient_type = Column(ENUM('composite', 'dairy', 'vegetable', 'meat', 'sauce', 'cereal', name="ingredient_type"), nullable=False)
    name = Column(VARCHAR, nullable=False)
    meal_uuid = Column(UUID(as_uuid=True), ForeignKey('meal.uuid', ondelete="CASCADE"))
    parent_uuid = Column(UUID(as_uuid=True), ForeignKey('meal_ingredient.uuid', ondelete="CASCADE"))

    sub_ingredient = relationship("MealIngredient")
