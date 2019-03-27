import os
import shutil
import sys
import re
from unittest.mock import patch

sys.path.append("./")
from podder_task_base.task_initializer.builders import GrpcTaskBuilder


class TestGrpcTaskFilecopyBuilder:
    TARGET_DIR = "tests/tmp"

    def setup_method(self, _method):
        if not os.path.exists(self.TARGET_DIR):
            os.mkdir(self.TARGET_DIR)

    def teardown_method(self, _method):
        if os.path.exists(self.TARGET_DIR):
            shutil.rmtree(self.TARGET_DIR)

    def test_filecopy_builder_execute_option_none(self):
        os.mkdir(os.path.join(self.TARGET_DIR, 'api'))

        file = "api/task_api.py"
        option = "test-sample-task"
        GrpcTaskBuilder().execute(self.TARGET_DIR, file, option)
        dst_path = os.path.join(self.TARGET_DIR, file)
        assert os.path.isfile(dst_path)

        with open(dst_path, "r") as f:
            out_str = f.read()

        task_class_match = re.search(r'task_class', out_str)
        test_sample_task_match = re.search(r'TestSampleTask', out_str)
        assert task_class_match == None
        assert test_sample_task_match != None
