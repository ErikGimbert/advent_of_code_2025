import pytest

from days.d05 import load_data
from tests.utils import with_tmp_file

# ===========================================================================
# MARK: Load Data
# ===========================================================================

EXAMPLE = """"""  # TODO add example input data
EXAMPLE_SPLIT = [
    # TODO add example input data
]


class TestLoadData:
    def test_load_from_tmp(self):
        def f(file_path: str) -> None:
            result = list(load_data(file_path))
            assert result == EXAMPLE_SPLIT

        with_tmp_file(EXAMPLE)(f)()

    def test_load_input(self):
        result = list(load_data())
        assert len(result) > 10


# ===========================================================================
# MARK: Part One
# ===========================================================================


class TestPartOne:
    EXAMPLE_EXPECTED = {
        # TODO add example input data
    }

    @pytest.mark.parametrize(
        "input",
        EXAMPLE,
    )
    def test_example(self, input):
        result = 0  # TODO replace with processing call
        assert result == self.EXAMPLE_EXPECTED[input]


# ===========================================================================
# MARK: Part Two
# ===========================================================================


class TestPartTwo:
    pass
