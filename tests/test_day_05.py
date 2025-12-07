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
        1: "spoiled",
        5: "fresh",
        8: "spoiled",
        11: "fresh",
        17: "fresh",
        32: "spoiled",
    }

    @pytest.mark.parametrize(
        "input",
        EXAMPLE_SPLIT.available_ids,
    )
    def test_example(self, input):
        result = "fresh" if EXAMPLE_SPLIT.is_fresh(input) else "spoiled"
        assert result == self.EXAMPLE_EXPECTED[input]

    def test_count_fresh(self):
        result = EXAMPLE_SPLIT.count_fresh()
        assert result == 3


# ===========================================================================
# MARK: Part Two
# ===========================================================================


class TestPartTwo:
    pass
