from pathlib import Path
from typing import Iterator

import utils.print as pr
from utils import file

DAY: int = 5
DAY_PADDED = f"{DAY:02d}"


def load_data(file_path: str | Path = file.input_path(DAY)) -> Iterator:
    input = file.to_list(file_path)
    # TODO implement data loading
    return input


# ==============================================================
# MARK: Part One
# ==============================================================


def part_one(input: Iterator) -> int:
    # TODO implement part one
    return 0


# ==============================================================
# MARK: Part Two
# ==============================================================


def part_two(input: Iterator) -> int:
    # TODO implement part two
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
    # input = load_data()
    # result = part_two(input)
    # pr.day(DAY, "Part Two: ", result)
