import os
import shutil
from unittest.mock import patch

from podder_task_base.task_initializer.podder_lib_install import PodderLibInstall


PODDER_LIB_INSTALL_MODULE = 'podder_task_base.task_initializer.podder_lib_install.PodderLibInstall'


class TestPodderLibInstall:
    TEST_TMP_PATH = './tests/tmp_test_builder'
    TASK_NAME = 'test-sample-task'
    TEST_DOWNLOAD_URL = "http://test/test/test"

    def teardown_method(self, _method):
        if os.path.exists(self.TEST_TMP_PATH):
            shutil.rmtree(self.TEST_TMP_PATH)

    def test_podder_lib_install(self):
        with patch(PODDER_LIB_INSTALL_MODULE + '._download_from_s3',
                   return_value=None) as _mock_download_from_s3:
            with patch(PODDER_LIB_INSTALL_MODULE + '._install_podder_lib',
                       return_value=None) as _mock_install_podder_lib:
                PodderLibInstall(self.TEST_DOWNLOAD_URL).execute()
                _mock_download_from_s3.assert_called_with(self.TEST_DOWNLOAD_URL)
                _mock_install_podder_lib.assert_called_with(None)
