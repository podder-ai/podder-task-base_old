import os
import click
import shutil
from stat import S_IRWXU, S_IRGRP, S_IXGRP, S_IROTH, S_IXOTH

from podder_task_base.task_initializer.builders import FilecopyBuilder
from podder_task_base.task_initializer.builders import MkdirBuilder
from podder_task_base.task_initializer.builders import TaskNameBuilder


class Builder(object):
    CHMOD755 = S_IRWXU | S_IRGRP | S_IXGRP | S_IROTH | S_IXOTH

    def __init__(self, task_name: str, target_dir: str) -> None:
        this_dir = os.path.dirname(os.path.abspath(__file__))
        self.templates_dir = os.path.join(this_dir, "./templates")
        self.target_dir = target_dir
        self.task_name = task_name
        if os.path.exists(target_dir):
            shutil.rmtree(target_dir)

    def init_task(self) -> None:
        print(self.templates_dir, self.target_dir)
        shutil.copytree(self.templates_dir, self.target_dir,
            ignore=shutil.ignore_patterns('__pycache__'))

        builders = [
            [MkdirBuilder   , 'config'                             , None],
            [MkdirBuilder   , 'input'                              , None],
            [MkdirBuilder   , 'output'                             , None],
            [MkdirBuilder   , 'tmp'                                , None],
            [MkdirBuilder   , 'error'                              , None],
            [FilecopyBuilder, 'run_codegen.py'                     , self.CHMOD755],
            [TaskNameBuilder, 'task_name.ini'                      , self.task_name],
            [FilecopyBuilder, 'scripts/entrypoint.sh'              , self.CHMOD755],
            [FilecopyBuilder, 'scripts/pre-commit.sh'              , self.CHMOD755],
            [FilecopyBuilder, 'scripts/restart_grpc_server.sh'     , self.CHMOD755],
            [TaskNameBuilder, 'api/task_api.py'                    , self.task_name],
            [TaskNameBuilder, 'api/grpc_server.py'                 , self.task_name],
            [TaskNameBuilder, 'api/protos/pipeline_framework.proto', self.task_name],
        ]
        self._build(
            builders=builders)

    def _build(self, builders: list) -> None:
        for builder, file, option in builders:
            builder(self.templates_dir).execute(self.target_dir, file, option)
        click.secho("{} : Completed successfully!".format(file), fg='green')
