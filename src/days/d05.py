from pathlib import Path
from typing import Any, Iterator

import utils.print as pr
from utils import file

DAY: int = 5
DAY_PADDED = f"{DAY:02d}"


class DataBase:
    _ranges: list[tuple[int, int]]
    _available_ids: list[int]
    _is_finalized: bool = False

    def __init__(
        self,
        ranges: list[tuple[int, int]] | None = None,
        available_ids: list[int] | None = None,
    ) -> None:
        self._ranges = ranges if ranges is not None else []
        self._available_ids = available_ids if available_ids is not None else []

    def add_range(self, range_tuple: tuple[int, int]) -> None:
        self._ranges.append(range_tuple)
        self._is_finalized = False

    def add_available_id(self, available_id: int) -> None:
        self._available_ids.append(available_id)
        self._is_finalized = False

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, DataBase):
            return False
        return (
            self._ranges == value._ranges
            and self._available_ids == value._available_ids
        )

    def _finalize_init(self) -> None:
        """Finalize initialization by sorting internal lists, if needed."""
        if self._is_finalized:
            return
        self._ranges.sort()
        self._available_ids.sort()
        self._is_finalized = True

    @property
    def available_ids(self) -> list[int]:
        """Get the list of available IDs, sorted."""
        self._finalize_init()
        return self._available_ids

    # === MARK: Part One methods

    def is_fresh(self, id: int) -> bool:
        """Check if the given ID is fresh (in any range)."""
        self._finalize_init()
        for start, end in self._ranges:
            if id < start:  # no need to check further, as ranges are sorted
                return False
            if start <= id <= end:
                return True
        return False

    def count_fresh(self) -> int:
        """Count how many available IDs are fresh."""
        count = 0
        for id in self._available_ids:
            if self.is_fresh(id):
                count += 1
        return count


def load_data(file_path: str | Path = file.input_path(DAY)) -> DataBase:
    input = DataBase()
    for line in file.to_list(file_path):
        line = line.strip()
        if "-" in line:
            start, end = line.split("-")
            input.add_range((int(start), int(end)))
        elif line.isdigit():
            input.add_available_id(int(line))
    input._finalize_init()
    return input


# ==============================================================
# MARK: Part One
# ==============================================================


def part_one(input: DataBase) -> int:
    return input.count_fresh()


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
