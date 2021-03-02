from sqlalchemy.dialects.postgresql import FLOAT
from sqlalchemy.sql.schema import Column, ColumnDefault, CheckConstraint


class ConsumableMixin(object):
    added_fat = Column(FLOAT, ColumnDefault(0.0), CheckConstraint("added_fat >= 0.0"))
    carbohydrates = Column(FLOAT, ColumnDefault(0.0), CheckConstraint("carbohydrates >= 0.0"))
    quantity = Column(FLOAT, CheckConstraint("quantity >= 0.0"), nullable=False)
