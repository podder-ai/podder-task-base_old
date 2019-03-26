import os
import shutil
import sys
from unittest.mock import patch

sys.path.append("./")
from podder_task_base.task_initializer.builder import Builder


def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)


def test_builder():
    target_dir = "./test_dir"
    task_name = "sample-task"
    try:
        Builder(task_name, target_dir).init_task()

        template_dir = './podder_task_base/task_initializer/templates'
        base_set = set()
        for file in find_all_files(template_dir):
            path = os.path.relpath(file, start=template_dir)
            base_set.add(path)

        test_set = set()
        for file in find_all_files(target_dir):
            path = os.path.relpath(file, start=target_dir)
            test_set.add(path)

        print("--base_set--")
        for path in sorted(base_set):
            print(path)
        print("--test_set--")
        for path in sorted(test_set):
            print(path)

        assert base_set == test_set

    finally:
        shutil.rmtree(target_dir)
