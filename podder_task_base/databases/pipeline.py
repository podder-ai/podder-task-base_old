from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from podder_task_base.settings import PIPELINE_DATABASE_URL

Engine = create_engine(PIPELINE_DATABASE_URL, echo=True)

sessionmaker(bind=Engine)
