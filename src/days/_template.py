from typing import Iterator

import utils.print as pr
from utils.file import file_to_list

DAY: int = 0
DAY_PADDED = f"{DAY:02d}"


def load_data(file_path: str) -> Iterator:
    input = file_to_list(file_path)
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
    input = load_data(f"./inputs/day_{DAY_PADDED}.txt")
    result = part_one(input)
    pr.day(DAY, "Part One: ", result)

    # Part Two
    # input = load_data(f"./inputs/day_{DAY_PADDED}.txt")
    # result = part_two(input)
    # pr.day(DAY, "Part Two: ", result)
