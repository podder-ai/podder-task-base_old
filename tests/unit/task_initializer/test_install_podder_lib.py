import os
import shutil
from unittest.mock import patch

from podder_task_base.task_initializer.install_podder_lib import InstallPodderLib


INSTALL_PODDER_LIB_MODULE = 'podder_task_base.task_initializer.install_podder_lib.InstallPodderLib'


class TestInstallPodderLib:
    TEST_TMP_PATH = './tests/tmp_test_builder'
    TASK_NAME = 'test-sample-task'

    def teardown_method(self, _method):
        if os.path.exists(self.TEST_TMP_PATH):
            shutil.rmtree(self.TEST_TMP_PATH)

    def test_install_podder_lib(self):
        with patch(INSTALL_PODDER_LIB_MODULE + '._get_download_url',
                   return_value=None) as _mock_get_download_url:
            with patch(INSTALL_PODDER_LIB_MODULE + '._download_from_s3',
                       return_value=None) as _mock_download_from_s3:
                with patch(INSTALL_PODDER_LIB_MODULE + '._install_podder_lib',
                           return_value=None) as _mock_install_podder_lib:
                    InstallPodderLib().execute()
                    _mock_get_download_url.assert_called_with()
                    _mock_download_from_s3.assert_called_with(None)
                    _mock_install_podder_lib.assert_called_with(None)
