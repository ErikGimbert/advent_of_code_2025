from pathlib import Path
from typing import Literal, Optional

import utils.print as pr
from utils import file

DAY: int = 6
DAY_PADDED = f"{DAY:02d}"


class Problem:
    _operator: Literal["+", "*"]
    _numbers: list[int]

    def __init__(self, operator: Literal["+", "*"] = "+", *numbers: int) -> None:
        self._operator = operator
        self._numbers = [*numbers]

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Problem):
            return False
        # Operations are bijective, so ideally we should sort numbers before comparing (but not necessary for puzzle solving)
        return self._operator == value._operator and self._numbers == value._numbers

    def len(self) -> int:
        return len(self._numbers)

    def set_operator(self, operator: Literal["+", "*"] | str) -> None:
        """Set the operator for the problem."""
        if operator not in ("+", "*"):
            raise ValueError("Operator must be '+' or '*'")
        self._operator = operator

    def append(self, number: int) -> None:
        """Append a number to the problem's number list."""
        self._numbers.append(number)

    def compute(self) -> int:
        """Compute the result based on the operator and numbers."""
        if self._operator == "+":
            return sum(self._numbers)
        elif self._operator == "*":
            result = 1
            for num in self._numbers:
                result *= num
            return result
        else:
            raise ValueError("Invalid operator")


class Homework:
    _problems: list[Problem]

    def __init__(self, *problem: Problem) -> None:
        self._problems = [*problem]

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Homework):
            return False
        return self._problems == value._problems

    def len(self) -> int:
        return len(self._problems)

    def _get_problem(self, index: int) -> Problem:
        while len(self._problems) <= index:
            self._problems.append(Problem())
        return self._problems[index]

    def set_operator(self, index: int, operator: Literal["+", "*"] | str) -> None:
        """Set the operator for a specific problem."""
        self._get_problem(index).set_operator(operator)

    def add_number(self, index: int, number: int) -> None:
        """Add a number to a specific problem."""
        self._get_problem(index).append(number)

    def sum_computations(self) -> int:
        """Sum the computations of all problems."""
        return sum(problem.compute() for problem in self._problems)


def load_data(file_path: str | Path = file.input_path(DAY)) -> Homework:
    input = file.to_list(file_path)
    homework = Homework()
    for line in input:
        parts = line.split()
        for col_index, part in enumerate(parts):
            if part in ("+", "*"):
                homework.set_operator(col_index, part)
            else:
                homework.add_number(col_index, int(part))
    return homework


# ==============================================================
# MARK: Part One
# ==============================================================


def part_one(input: Homework) -> int:
    return input.sum_computations()


# ==============================================================
# MARK: Part Two
# ==============================================================


def part_two(input: Homework) -> int:
    raise NotImplementedError  # TODO implement part two
    return 0


# ==============================================================
# MARK: Main function
# ==============================================================


def run():
    # Part One
    input = load_data()
    result = part_one(input)
    pr.day(DAY, "Part One: ", result)

    # Part Two
    try:
        result = part_two(input)
        pr.day(DAY, "Part Two: ", result)
    except NotImplementedError:
        pr.info("Part Two not implemented yet.")
