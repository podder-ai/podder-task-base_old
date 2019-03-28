from click.testing import CliRunner
from unittest.mock import patch

from podder_task_base.task_initializer import __main__


runner = CliRunner()


BUILDER_MODULE = 'podder_task_base.task_initializer.builder.Builder'


def test_main_task_initializer_init():
    with patch(BUILDER_MODULE + '.__init__') as _mock_init:
        _mock_init.return_value = None
        with patch(BUILDER_MODULE + '.init_task') as _mock_init_task:
            _mock_init_task.return_value = None

            target_dir = "./test_dir"
            task_name = "sample-task"
            result = runner.invoke(__main__.init, [task_name, "--target-dir=%s"%target_dir])

            assert not result.exception

            assert _mock_init.call_count == 1
            args, kwargs = _mock_init.call_args
            assert args == (task_name, target_dir)

            assert _mock_init_task.call_count == 1
            args, kwargs = _mock_init_task.call_args
            assert args == ()
