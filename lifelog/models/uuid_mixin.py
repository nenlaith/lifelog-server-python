import uuid

from sqlalchemy import Column, ForeignKey, ColumnDefault
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import has_inherited_table, declared_attr

from lifelog.main.util import get_parent_tablename_by_bases


class UUIDMixin(object):
    @declared_attr.cascading
    def uuid(cls):
        parent_tablename = get_parent_tablename_by_bases(cls.__bases__)
        if has_inherited_table(cls) and parent_tablename != '':
            return Column(ForeignKey(parent_tablename + '.uuid'), primary_key=True)
        else:
            return Column(UUID(as_uuid=True), ColumnDefault(uuid.uuid4), primary_key=True)
