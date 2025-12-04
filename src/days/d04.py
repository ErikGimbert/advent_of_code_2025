from enum import Enum, Flag, StrEnum, auto
from pathlib import Path
from typing import Iterable, Iterator, Literal, Optional, Union

import utils.print as pr
from utils import file

DAY: int = 4
DAY_PADDED = f"{DAY:02d}"


class RollState(StrEnum):
    ROLL = "@"
    NONE = "."
    ROLL_ACCESSIBLE = "x"

    def __or__(self, other: object) -> set["RollState"]:
        if not isinstance(other, RollState) and not isinstance(other, set):
            return NotImplemented
        if isinstance(other, set):
            return {self} | other
        if isinstance(other, RollState):
            return {self, other}


class Grid:
    __gird: list[list[RollState]]

    def __init__(self, data: Iterable[str]) -> None:
        self.__gird = []
        for line in data:
            l_list: list[RollState] = []
            for c in line.strip():
                l_list.append(RollState(c))
            self.__gird.append(l_list)

    def __str__(self) -> str:
        return "\n".join("".join(map(str, row)) for row in self.__gird)

    def __len__(self) -> int:
        return sum(len(row) for row in self.__gird)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Grid):
            return False
        for y in range(len(self.__gird)):
            for x in range(len(self.__gird[y])):
                assert self.__gird[y][x] == other.__gird[y][x], (
                    f"Mismatch at ({x}, {y}): {self.__gird[y][x].name} != {other.__gird[y][x].name}"
                )
        return True

    def __iter__(self) -> Iterator[tuple[int, int, RollState]]:
        for y in range(len(self.__gird)):
            for x in range(len(self.__gird[y])):
                yield (x, y, self.__gird[y][x])

    def copy(self) -> "Grid":
        """Return a copy of the grid."""
        data = ["".join(str(cell) for cell in row) for row in self.__gird]
        return Grid(data)

    def mark_as_accessible(self, x: int, y: int) -> None:
        """Mark the roll at (x, y) as accessible."""
        self.__gird[y][x] = RollState.ROLL_ACCESSIBLE

    def neighbors(
        self, x: int, y: int, state: Optional[RollState | set[RollState]] = None
    ) -> list[tuple[int, int, RollState]]:
        """Return the neighbors of the cell at (x, y). If state is provided, only return neighbors with that state."""
        if state is not None and not isinstance(state, set):
            state = {state}

        neighbors = []
        directions = [  # 8 directions
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= ny < len(self.__gird) and 0 <= nx < len(self.__gird[ny]):
                if state is None or self.__gird[ny][nx] in state:
                    neighbors.append((nx, ny, self.__gird[ny][nx]))

        return neighbors

    def count(self, state: RollState | set[RollState]) -> int:
        """Count the number of cells with the given state(s)."""
        if not isinstance(state, set):
            state = {state}
        count = 0
        for _, _, cell_state in self:
            if cell_state in state:
                count += 1
        return count


def load_data(file_path: str | Path = file.input_path(DAY)) -> Grid:
    input = file.to_list(file_path)
    return Grid(input)


# ==============================================================
# MARK: Part One
# ==============================================================


def mark_accessible_rolls(grid: Grid) -> None:
    for x, y, state in grid:
        if state != RollState.ROLL:
            continue
        neighbors = grid.neighbors(x, y, RollState.ROLL | RollState.ROLL_ACCESSIBLE)
        if len(neighbors) < 4:  # less than 4 neighboring rolls
            grid.mark_as_accessible(x, y)


def part_one(input: Grid) -> int:
    mark_accessible_rolls(input)
    return input.count(RollState.ROLL_ACCESSIBLE)


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
