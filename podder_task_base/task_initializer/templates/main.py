from app import Task
from podder_task_base import Context
from podder_task_base.services import InputsService
from podder_task_base import settings

DAG_ID = "___dag_id___"


def execute() -> None:
    settings.init()
    context = Context(DAG_ID)
    task = Task(context)
    inputs = InputsService(context).create()
    task.execute(inputs)


if __name__ == "__main__":
    execute()