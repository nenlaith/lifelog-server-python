import datetime

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import has_inherited_table
from sqlalchemy.orm import sessionmaker, scoped_session

from flask import _app_ctx_stack

from lifelog.main.util import is_parent_table

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres@/lifelog?host=/run/postgresql'
engine = create_engine(
    SQLALCHEMY_DATABASE_URI
    # ,connect_args={
    #     "check_same_thread": False
    # }
)


def get_session():

    sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = scoped_session(sessionlocal(), scopefunc=_app_ctx_stack.__ident_func__)

    from sqlalchemy import event

    @event.listens_for(session, 'before_flush')
    def receive_before_flush(sess, _flush_context, _instances):
        for x in sess.dirty:
            if has_inherited_table(x.__class__) or is_parent_table(x.__class__):
                x.updated_at = datetime.datetime.now()

    return session
