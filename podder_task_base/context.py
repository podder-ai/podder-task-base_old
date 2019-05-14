from podder_task_base.databases.pipeline import Session as PipelineSession
from podder_task_base.databases.pipeline import ROSession as PipelineROSession

from .config import Config
from .file import File


class Context(object):
    def __init__(self, dag_id: str) -> None:
        self.config = Config()
        self.file = File()
        self.session = PipelineSession()
        self.ro_session = PipelineROSession()
        self.dag_id = dag_id
