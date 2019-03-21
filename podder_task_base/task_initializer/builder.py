import click
from stat import S_IRWXU, S_IRGRP, S_IXGRP, S_IROTH, S_IXOTH

from podder_task_base.task_initializer.builders import FilecopyBuilder
from podder_task_base.task_initializer.builders import MkdirBuilder


class Builder(object):
    CHMOD755 = S_IRWXU | S_IRGRP | S_IXGRP | S_IROTH | S_IXOTH

    def __init__(self, target_dir: str) -> None:
        self.target_dir = target_dir

    def init_task(self) -> None:
        builders = [
            [FilecopyBuilder, 'requirements.default.txt'           , None],
            [FilecopyBuilder, 'pytest.ini'                         , None],
            [FilecopyBuilder, 'run_codegen.py'                     , self.CHMOD755],
            [MkdirBuilder   , 'api'                                , None],
            [FilecopyBuilder, 'api/__init__.py'                    , None],
            [FilecopyBuilder, 'api/task_api.py'                    , None],
            [FilecopyBuilder, 'api/grpc_server.py'                 , None],
            [MkdirBuilder   , 'api/protos'                         , None],
            [FilecopyBuilder, 'api/protos/__init__.py'             , None],
            [FilecopyBuilder, 'api/protos/pipeline_framework.proto', None],
            [MkdirBuilder   , 'scripts'                            , None],
            [FilecopyBuilder, 'scripts/entrypoint.sh'              , self.CHMOD755],
            [FilecopyBuilder, 'scripts/pre-commit.sh'              , self.CHMOD755],
            [FilecopyBuilder, 'scripts/restart_grpc_server.sh'     , self.CHMOD755],
            [MkdirBuilder   , 'config'                             , None],
            [MkdirBuilder   , 'input'                              , None],
            [MkdirBuilder   , 'output'                             , None],
            [MkdirBuilder   , 'tmp'                                , None],
            [MkdirBuilder   , 'error'                              , None],
        ]
        self._build(
            builders=builders)

    def _build(self, builders: list) -> None:
        for builder, file, option in builders:
            builder().execute(self.target_dir, file, option)
        click.secho("{} : Completed successfully!".format(file), fg='green')
