from pathlib import Path
from typing import Final, Iterator

import utils.print as pr
from utils import file

DAY: int = 3
DAY_PADDED = f"{DAY:02d}"


def load_data(file_path: str | Path) -> Iterator:
    input = file.to_list(file_path)
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
    """Sum of max joltage for each bank"""
    return sum(map(p2_max_joltage, banks))


def p2_max_joltage(bank: str) -> int:
    """Calculate the maximum joltage for a given bank string."""
    batteries = [int(x) for x in bank]
    len_bank = len(batteries)
    NB_DIGITS: Final[int] = 12
    prev_idx = -1
    res: str = ""
    for i in range(NB_DIGITS):
        digit = max(batteries[prev_idx + 1 : len_bank - (NB_DIGITS - 1 - i)])
        prev_idx = batteries.index(digit, prev_idx + 1)
        res += str(digit)

    return int(res)


# ==============================================================
# MARK: Main function
# ==============================================================


def run():
    input_path = file.input_path(DAY)

    # Part One
    banks = load_data(input_path)
    result = part_one(banks)
    pr.day(DAY, "Part One: ", result)

    # Part Two
    banks = load_data(input_path)
    result = part_two(banks)
    pr.day(DAY, "Part Two: ", result)
