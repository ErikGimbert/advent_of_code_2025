import itertools
import re
from functools import reduce
from typing import Iterator

from utils.file import file_to_list
from utils.print import pr_day


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


def run():
    ids_range = load_data("./inputs/day_02.txt")
    result = sum_invalid_ids(ids_range)
    pr_day(2, "Sum of invalid IDs:", result)


if __name__ == "__main__":
    run()
