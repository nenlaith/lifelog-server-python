from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column, ColumnDefault
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.types import TIMESTAMP
import uuid
import datetime

class Element(object):
    __tablename__ = 'element'

    uuid = Column(UUID(as_uuid=True), ColumnDefault(uuid.uuid4), primary_key=True)
    created_at = Column(TIMESTAMP(timezone=True), ColumnDefault(datetime.datetime.now))
    updated_at = Column(TIMESTAMP(timezone=True), ColumnDefault(datetime.datetime.now, for_update=True))


Base = declarative_base(cls=Element)