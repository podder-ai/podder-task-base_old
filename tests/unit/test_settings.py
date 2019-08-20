from unittest.mock import patch

import pytest

from podder_lib.settings import get, init


class TestSettings:
    def test_init_method_does_not_raise_an_error(self):
        init()
