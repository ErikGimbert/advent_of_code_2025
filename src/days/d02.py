import itertools
import re
from typing import Iterator

import utils.print as pr
from utils.file import file_to_list


def load_data(file_path: str) -> Iterator[tuple[int, int]]:
    ids_range = file_to_list(file_path, sep=",")
    for r in ids_range:
        try:
            a, b = r.split("-")
            yield int(a), int(b)
        except ValueError as e:
            raise ValueError(f"Invalid range: {r}, error: {e}")


RE_INVALID_ID = re.compile(r"^(\d+)\1$")


def find_invalid_ids(ids_range: tuple[int, int]) -> Iterator[int]:
    for id in range(ids_range[0], ids_range[1] + 1):
        if RE_INVALID_ID.match(str(id)):
            yield id


def sum_invalid_ids(ids_range: Iterator[tuple[int, int]]) -> int:
    return sum(itertools.chain.from_iterable(map(find_invalid_ids, ids_range)))


# ==============================================================
# Part Two
# ==============================================================

RE_INVALID_ID_V2 = re.compile(r"^(\d+)\1+$")


def find_invalid_ids_v2(ids_range: tuple[int, int]) -> Iterator[int]:
    for id in range(ids_range[0], ids_range[1] + 1):
        if RE_INVALID_ID_V2.match(str(id)):
            yield id


def sum_invalid_ids_v2(ids_range: Iterator[tuple[int, int]]) -> int:
    return sum(itertools.chain.from_iterable(map(find_invalid_ids_v2, ids_range)))


# ==============================================================
# Main function
# ==============================================================


def run():
    ids_range = load_data("./inputs/day_02.txt")
    result = sum_invalid_ids(ids_range)
    pr.day(2, "Part One: Sum of invalid IDs:", result)

    # Part Two
    ids_range = load_data("./inputs/day_02.txt")
    result = sum_invalid_ids_v2(ids_range)
    pr.day(2, "Part Two: Sum of invalid IDs:", result)
