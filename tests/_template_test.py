import pytest  # noqa: F401

from days._template import load_data
from tests.utils import with_tmp_file

# ===========================================================================
# MARK: Part One
# ===========================================================================


class TestLoadData:
    def test_load_data(self):
        def f(file_path: str) -> None:
            result = list(load_data(file_path))
            assert result == []

        with_tmp_file("""""")(f)()


# TODO add tests for part one

# ===========================================================================
# MARK: Part Two
# ===========================================================================

# TODO add tests for part two
