from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import ENUM, VARCHAR, UUID
from sqlalchemy.orm import relationship

from swagger_server.models.consumable_mixin import ConsumableMixin
from swagger_server.models.element_base import ElementBase


class MealIngredient(ElementBase, ConsumableMixin):
    __mapper_args__ = {
        'column_prefix': __tablename__ + '_'
    }

    category = Column(ENUM('composite', 'dairy', 'vegetable', 'meat', 'sauce', 'cereal'), nullable=False)
    name = Column(VARCHAR, nullable=False)
    meal_uuid = Column(UUID(as_uuid=True), ForeignKey('meal.uuid', ondelete="CASCADE"))
    parent_uuid = Column(UUID(as_uuid=True), ForeignKey('meal_ingredient.uuid', ondelete="CASCADE"))

    sub_ingredient = relationship("MealIngredient")
