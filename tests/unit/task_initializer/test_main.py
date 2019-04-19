import os
import shutil

from click.testing import CliRunner
from unittest.mock import patch

from podder_task_base.task_initializer import __main__


runner = CliRunner()


BUILDER_MODULE = 'podder_task_base.task_initializer.builder.Builder'
PODDER_LIB_INSTALL_MODULE = 'podder_task_base.task_initializer.podder_lib_install.PodderLibInstall'

class TestMain():
    TEST_TMP_PATH = "test_dir"
    TEST_TASK_NAME = "sample-task"

    def teardown_method(self, _method):
        if os.path.exists(self.TEST_TMP_PATH):
            shutil.rmtree(self.TEST_TMP_PATH)

    def test_main_task_initializer_init(self):
        with patch(PODDER_LIB_INSTALL_MODULE + '.__init__') as _mock_install_init:
            _mock_install_init.return_value = None
            with patch(PODDER_LIB_INSTALL_MODULE + '.execute') as _mock_install_execute:
                _mock_install_execute.return_value = None

                with patch(BUILDER_MODULE + '.__init__') as _mock_builder_init:
                    _mock_builder_init.return_value = None
                    with patch(BUILDER_MODULE + '.init_task') as _mock_builder_init_task:
                        _mock_builder_init_task.return_value = None

                        target_dir = self.TEST_TMP_PATH
                        task_name = self.TEST_TASK_NAME
                        result = runner.invoke(__main__.init,
                            [task_name, "--target-dir=%s"%target_dir])

                        assert not result.exception
                        _mock_builder_init.assert_called_with(task_name, target_dir)
                        _mock_builder_init_task.assert_called_with()

                        _mock_install_init.assert_called_with()
                        _mock_install_execute.assert_called_with()
