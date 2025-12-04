import pytest  # noqa: F401

from days.d04 import (
    Grid,
    RollState,
    load_data,
    mark_accessible_rolls,
    part_one,
    part_two,
    remove_accessible_rolls,
)
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
        result = part_one(EXAMPLE_SPLIT.copy())
        assert result == self.EXAMPLE_RESULT


# ===========================================================================
# MARK: Part Two
# ===========================================================================


class TestPartTwo:
    EXAMPLE_STEP_EXPECTED = {
        1: {
            "roll_removed": 13,
            "grid": Grid(
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
            ),
        },
        2: {
            "roll_removed": 12,
            "grid": Grid(
                [
                    ".......x..",
                    ".@@.x.x.@x",
                    "x@@@@...@@",
                    "x.@@@@..x.",
                    ".@.@@@@.x.",
                    ".x@@@@@@.x",
                    ".x.@.@.@@@",
                    "..@@@.@@@@",
                    ".x@@@@@@@.",
                    "....@@@...",
                ]
            ),
        },
        3: {
            "roll_removed": 7,
            "grid": Grid(
                [
                    "..........",
                    ".x@.....x.",
                    ".@@@@...xx",
                    "..@@@@....",
                    ".x.@@@@...",
                    "..@@@@@@..",
                    "...@.@.@@x",
                    "..@@@.@@@@",
                    "..x@@@@@@.",
                    "....@@@...",
                ]
            ),
        },
        4: {
            "roll_removed": 5,
            "grid": Grid(
                [
                    "..........",
                    "..x.......",
                    ".x@@@.....",
                    "..@@@@....",
                    "...@@@@...",
                    "..x@@@@@..",
                    "...@.@.@@.",
                    "..x@@.@@@x",
                    "...@@@@@@.",
                    "....@@@...",
                ]
            ),
        },
        5: {
            "roll_removed": 2,
            "grid": Grid(
                [
                    "..........",
                    "..........",
                    "..x@@.....",
                    "..@@@@....",
                    "...@@@@...",
                    "...@@@@@..",
                    "...@.@.@@.",
                    "...@@.@@@.",
                    "...@@@@@x.",
                    "....@@@...",
                ]
            ),
        },
        6: {
            "roll_removed": 1,
            "grid": Grid(
                [
                    "..........",
                    "..........",
                    "...@@.....",
                    "..x@@@....",
                    "...@@@@...",
                    "...@@@@@..",
                    "...@.@.@@.",
                    "...@@.@@@.",
                    "...@@@@@..",
                    "....@@@...",
                ]
            ),
        },
        7: {
            "roll_removed": 1,
            "grid": Grid(
                [
                    "..........",
                    "..........",
                    "...x@.....",
                    "...@@@....",
                    "...@@@@...",
                    "...@@@@@..",
                    "...@.@.@@.",
                    "...@@.@@@.",
                    "...@@@@@..",
                    "....@@@...",
                ]
            ),
        },
        8: {
            "roll_removed": 1,
            "grid": Grid(
                [
                    "..........",
                    "..........",
                    "....x.....",
                    "...@@@....",
                    "...@@@@...",
                    "...@@@@@..",
                    "...@.@.@@.",
                    "...@@.@@@.",
                    "...@@@@@..",
                    "....@@@...",
                ]
            ),
        },
        9: {
            "roll_removed": 1,
            "grid": Grid(
                [
                    "..........",
                    "..........",
                    "..........",
                    "...x@@....",
                    "...@@@@...",
                    "...@@@@@..",
                    "...@.@.@@.",
                    "...@@.@@@.",
                    "...@@@@@..",
                    "....@@@...",
                ]
            ),
        },
    }
    EXAMPLE_RESULT = 43

    def test_part_two_steps(self):
        grid = EXAMPLE_SPLIT.copy()
        for step in range(1, 10):
            mark_accessible_rolls(grid)
            expected = self.EXAMPLE_STEP_EXPECTED[step]
            assert grid.count(RollState.ROLL_ACCESSIBLE) == expected["roll_removed"], (
                f"Step {step} did not match expected roll accessible."
            )
            assert grid == expected["grid"], f"Step {step} did not match expected grid."
            removed = remove_accessible_rolls(grid)
            assert removed == expected["roll_removed"], (
                f"Step {step} did not match expected removed rolls."
            )

    def test_part(self):
        result = part_two(EXAMPLE_SPLIT.copy())
        assert result == self.EXAMPLE_RESULT
