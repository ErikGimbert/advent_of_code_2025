import pytest

from days.d05 import DataBase, load_data
from tests.utils import with_tmp_file

# ===========================================================================
# MARK: Load Data
# ===========================================================================

EXAMPLE = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""
EXAMPLE_SPLIT = DataBase(
    ranges=[(3, 5), (10, 14), (16, 20), (12, 18)],
    available_ids=[1, 5, 8, 11, 17, 32],
)


class TestLoadData:
    def test_load_from_tmp(self):
        def f(file_path: str) -> None:
            result = load_data(file_path)
            assert result == EXAMPLE_SPLIT

        with_tmp_file(EXAMPLE)(f)()

    def test_load_input(self):
        result = load_data()
        assert len(result._ranges) > 10


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
        # assert result == self.EXAMPLE_EXPECTED[input]


# ===========================================================================
# MARK: Part Two
# ===========================================================================


class TestPartTwo:
    pass
