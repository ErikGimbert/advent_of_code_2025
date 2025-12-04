import pytest  # noqa: F401

from days._template import load_data
from tests.utils import with_tmp_file

# ===========================================================================
# MARK: Part One
# ===========================================================================


class TestLoadData:
    def test_load_from_tmp(self):
        def f(file_path: str) -> None:
            result = list(load_data(file_path))
            assert result == []

        with_tmp_file("""""")(f)()

    def test_load_input(self):
        result = list(load_data())
        assert len(result) > 1000


# TODO add tests for part one

# ===========================================================================
# MARK: Part Two
# ===========================================================================

# TODO add tests for part two
