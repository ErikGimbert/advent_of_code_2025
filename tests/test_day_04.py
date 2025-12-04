import pytest  # noqa: F401

from days.d04 import Grid, RollState, load_data, mark_accessible_rolls
from tests.utils import with_tmp_file

# ===========================================================================
# MARK: Load Data
# ===========================================================================


EXAMPLE = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""
EXAMPLE_SPLIT = Grid(
    [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@.",
    ]
)


class TestLoadData:
    def test_load_from_tmp(self):
        def f(file_path: str) -> None:
            result = load_data(file_path)
            assert result == EXAMPLE_SPLIT

        with_tmp_file(EXAMPLE)(f)()

    def test_load_input(self):
        result = load_data()
        assert len(result) > 10


# ===========================================================================
# MARK: Part One
# ===========================================================================


class TestPartOne:
    EXAMPLE_EXPECTED = Grid(
        [
            "..xx.xx@x.",
            "x@@.@.@.@@",
            "@@@@@.x.@@",
            "@.@@@@..@.",
            "x@.@@@@.@x",
            ".@@@@@@@.@",
            ".@.@.@.@@@",
            "x.@@@.@@@@",
            ".@@@@@@@@.",
            "x.x.@@@.x.",
        ]
    )
    EXAMPLE_RESULT = 13

    def test_mark_accessible_rolls(self):
        result = EXAMPLE_SPLIT.copy()
        mark_accessible_rolls(result)
        assert result == self.EXAMPLE_EXPECTED

    def test_part(self):
        result = EXAMPLE_SPLIT.copy()
        mark_accessible_rolls(result)
        assert result.count(RollState.ROLL_ACCESSIBLE) == self.EXAMPLE_RESULT


# ===========================================================================
# MARK: Part Two
# ===========================================================================


class TestPartTwo:
    pass
