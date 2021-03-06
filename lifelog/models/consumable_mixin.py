from sqlalchemy.dialects.postgresql import REAL
from sqlalchemy.sql.schema import Column, ColumnDefault, CheckConstraint


class ConsumableMixin(object):
    added_fat = Column(REAL, ColumnDefault(0.0), CheckConstraint("added_fat >= 0.0"))
    carbohydrates = Column(REAL, ColumnDefault(0.0), CheckConstraint("carbohydrates >= 0.0"))
    quantity = Column(REAL, CheckConstraint("quantity >= 0.0"), nullable=False)
