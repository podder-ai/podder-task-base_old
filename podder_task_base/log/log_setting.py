import logging
import os

import yaml


class LogSetting:
    LOG_YML_PATH = 'log.yml'

    def __init__(self):
        pass

    def load(self):
        global _log_setting
        if _log_setting is None:
            _log_setting = self._load_log_yml()
        return(_log_setting)

    def _load_log_yml(self):
        file_path = self.LOG_YML_PATH
        if os.path.exists(file_path):
            with open(file_path, 'r') as stream:
                ret = yaml.load(stream)
        else:
            # load defalut values
            ret = {
                "task_name": "task-name-sample",
                "task_log_format": "%(asctime)s:%(levelname)s:%(message)s",
                "task_log_level": logging.DEBUG,
                "sql_log_format": "%(asctime)s:%(levelname)s:%(message)s",
                "sql_log_level": logging.INFO,
            }

        return ret

_log_setting = None
