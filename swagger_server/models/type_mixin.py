from sqlalchemy import Column, ColumnDefault
from sqlalchemy.dialects.postgresql import VARCHAR
from sqlalchemy.ext.declarative import declared_attr

from swagger_server.util import is_parent_table

class TypeMixin(object):
    @declared_attr
    def type(cls):
        return Column(VARCHAR, ColumnDefault(cls.__tablename__), nullable=False)
