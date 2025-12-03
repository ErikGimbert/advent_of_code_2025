from typing import Iterator

import utils.print as pr
from utils.file import file_to_list

DAY: int = 3
DAY_PADDED = f"{DAY:02d}"


def load_data(file_path: str) -> Iterator:
    input = file_to_list(file_path)
    return input


# ==============================================================
# MARK: Part One
# ==============================================================


def part_one(banks: Iterator) -> int:
    """Sum of max joltage for each bank"""
    return sum(map(p1_max_joltage, banks))


def p1_max_joltage(bank: str) -> int:
    """Calculate the maximum joltage for a given bank string."""
    batteries = [int(x) for x in bank]
    tens = max(
        batteries[:-1]
    )  # exclude the last element (we need at least one for unit digit)
    idx_tens = batteries.index(tens)
    unit = max(batteries[idx_tens + 1 :])  # exclude all elements before idx_tens
    return tens * 10 + unit


# ==============================================================
# MARK: Part Two
# ==============================================================


def part_two(banks: Iterator) -> int:
    # TODO implement part two
    return 0


# ==============================================================
# MARK: Main function
# ==============================================================


def run():
    banks = load_data(f"./inputs/day_{DAY_PADDED}.txt")
    result = part_one(banks)
    pr.day(DAY, "Part One: ", result)

    # Part Two
    # banks = load_data(f"./inputs/day_{DAY_PADDED}.txt")
    # result = part_two(banks)
    # pr.day(DAY, "Part Two: ", result)
