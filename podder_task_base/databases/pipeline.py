from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import sessionmaker

from podder_task_base.settings import PIPELINE_DATABASE_URL

from . import log


engine: Engine = create_engine(PIPELINE_DATABASE_URL, echo=False)

Session: DeclarativeMeta = sessionmaker(bind=engine)
