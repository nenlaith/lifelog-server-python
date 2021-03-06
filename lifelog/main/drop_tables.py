from lifelog.main.database import Engine

from lifelog.models import *

element_base.ElementBase.metadata.drop_all(Engine)
