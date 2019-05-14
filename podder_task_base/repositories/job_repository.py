from typing import Any, List

from sqlalchemy.orm.session import Session

from podder_task_base.models.pipeline import JobModel
from podder_task_base.repositories.base import BaseRepository


class JobRepository(BaseRepository):

    model_class = JobModel
    RUNNING_STATUS = 'running'
    COMPLETE_STATUS = 'complete'

    @property
    def session(self) -> Session:
        return self.context.session

    @property
    def ro_session(self) -> Session:
        return self.context.ro_session

    def find_all(self) -> List[Any]:
        if self.ro_session:
            return self.ro_session.query(self.model_class).all()
        return self.session.query(self.model_class).all()

    def find_by_unique_key(self, job_id: str) -> JobModel:
        if self.ro_session:
            return self.ro_session.query(self.model_class).filter(
                self.model_class.job_id == job_id).one_or_none()
        return self.session.query(self.model_class).filter(
            self.model_class.job_id == job_id).one_or_none()

    def find_by_dag_id(self, dag_id: str) -> List[Any]:
        if self.ro_session:
            return self.ro_session.query(self.model_class).filter(
                self.model_class.dag_id == dag_id)   
        return self.session.query(self.model_class).filter(
            self.model_class.dag_id == dag_id)
