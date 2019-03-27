import os
import shutil
import sys
from stat import S_IRWXU, S_IRGRP, S_IXGRP, S_IROTH, S_IXOTH, filemode
from unittest.mock import patch

sys.path.append("./")
from podder_task_base.task_initializer.builders import FilecopyBuilder


class TestFilecopyBuilder:
    TARGET_DIR = "tests/tmp"
    CHMOD755 = S_IRWXU | S_IRGRP | S_IXGRP | S_IROTH | S_IXOTH

    def setup_method(self, _method):
        if not os.path.exists(self.TARGET_DIR):
            os.mkdir(self.TARGET_DIR)

    def teardown_method(self, _method):
        if os.path.exists(self.TARGET_DIR):
            shutil.rmtree(self.TARGET_DIR)

    def test_filecopy_builder_execute_option_none(self):
        file = "__init__.py"
        option = None
        FilecopyBuilder().execute(self.TARGET_DIR, file, option)
        assert os.path.isfile(os.path.join(self.TARGET_DIR, file))

    def test_filecopy_builder_execute_option_755(self):
        file = "__init__.py"
        option = self.CHMOD755
        FilecopyBuilder().execute(self.TARGET_DIR, file, option)

        dst_path = os.path.join(self.TARGET_DIR, file)
        assert os.path.exists(dst_path)

        statinfo = os.stat(dst_path)
        mode = statinfo.st_mode
        assert filemode(mode) == '-rwxr-xr-x'
