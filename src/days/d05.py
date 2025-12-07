from pathlib import Path
from typing import Iterator

import utils.print as pr
from utils import file

DAY: int = 5
DAY_PADDED = f"{DAY:02d}"


class DataBase:
    _ranges: list[tuple[int, int]]
    _available_ids: list[int]

    def __init__(
        self,
        ranges: list[tuple[int, int]] | None = None,
        available_ids: list[int] | None = None,
    ) -> None:
        self._ranges = ranges if ranges is not None else []
        self._available_ids = available_ids if available_ids is not None else []

    def add_range(self, range_tuple: tuple[int, int]) -> None:
        self._ranges.append(range_tuple)

    def add_available_id(self, available_id: int) -> None:
        self._available_ids.append(available_id)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, DataBase):
            return False
        return (
            self._ranges == value._ranges
            and self._available_ids == value._available_ids
        )


def load_data(file_path: str | Path = file.input_path(DAY)) -> DataBase:
    input = DataBase()
    for line in file.to_list(file_path):
        line = line.strip()
        if "-" in line:
            start, end = line.split("-")
            input.add_range((int(start), int(end)))
        elif line.isdigit():
            input.add_available_id(int(line))

    return input


# ==============================================================
# MARK: Part One
# ==============================================================


def part_one(input: DataBase) -> int:
    # TODO implement part one
    return 0


# ==============================================================
# MARK: Part Two
# ==============================================================


def part_two(input: DataBase) -> int:
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
