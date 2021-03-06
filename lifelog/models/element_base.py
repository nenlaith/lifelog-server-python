import datetime
import regex

from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base, declared_attr, has_inherited_table
from sqlalchemy.sql.schema import Column, ColumnDefault

from lifelog.main.util import get_parent_tablename_by_bases, is_parent_table


class Element(object):
    @declared_attr
    def __tablename__(cls):
        return '_'.join(str.lower(string) for string in regex.findall('[A-Z]+[a-z]+', cls.__name__))

    @declared_attr
    def __mapper_args__(cls):
        parent_tablename = get_parent_tablename_by_bases(cls.__bases__)
        if has_inherited_table(cls) and parent_tablename != '':
            return {
                'polymorphic_identity': cls.__tablename__
            }
        elif is_parent_table(cls):
            return {
                'polymorphic_on': cls.__tablename__ + '_type',
                'polymorphic_identity': cls.__tablename__
            }
        else:
            return {}

    created_at = Column(TIMESTAMP(timezone=True), ColumnDefault(datetime.datetime.now), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), ColumnDefault(datetime.datetime.now), nullable=False)


ElementBase = declarative_base(cls=Element)
