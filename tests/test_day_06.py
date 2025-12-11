import pytest

from days.d06 import Homework, Problem, load_data
from tests.utils import with_tmp_file

# ===========================================================================
# MARK: Load Data
# ===========================================================================

EXAMPLE = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""
EXAMPLE_SPLIT = Homework(
    Problem("*", 123, 45, 6),
    Problem("+", 328, 64, 98),
    Problem("*", 51, 387, 215),
    Problem("+", 64, 23, 314),
)


class TestLoadData:
    def test_load_from_tmp(self):
        def f(file_path: str) -> None:
            result = load_data(file_path)
            assert result == EXAMPLE_SPLIT
            assert result.len() == 4
            for problem in result._problems:
                assert problem.len() == 3

        with_tmp_file(EXAMPLE)(f)()

    def test_load_input(self):
        result = load_data()
        assert result.len() > 10


# ===========================================================================
# MARK: Part One
# ===========================================================================


class TestPartOne:
    EXAMPLE_EXPECTED = [
        (Problem("*", 123, 45, 6), 33210),
        (Problem("+", 328, 64, 98), 490),
        (Problem("*", 51, 387, 215), 4243455),
        (Problem("+", 64, 23, 314), 401),
    ]

    @pytest.mark.parametrize(
        "problem,expected",
        EXAMPLE_EXPECTED,
    )
    def test_example(self, problem: Problem, expected: int):
        assert problem.compute() == expected

    def test_example_total(self):
        assert EXAMPLE_SPLIT.sum_computations() == 4277556


# ===========================================================================
# MARK: Part Two
# ===========================================================================


class TestPartTwo:
    pass
