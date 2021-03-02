from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.sql.schema import Column, ColumnDefault
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
import uuid
import datetime


class Element(object):
    @declared_attr
    def __tablename__(cls):
        return '_'.join(str.lower(string) for string in re.findall('[A-Z]+[a-z]+', cls.__name__))

    uuid = Column(UUID(as_uuid=True), ColumnDefault(uuid.uuid4), primary_key=True)
    created_at = Column(TIMESTAMP(timezone=True), ColumnDefault(datetime.datetime.now))
    updated_at = Column(TIMESTAMP(timezone=True), ColumnDefault(datetime.datetime.now, for_update=True))


ElementBase = declarative_base(cls=Element)
