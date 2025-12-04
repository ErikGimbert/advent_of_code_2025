from pathlib import Path
from typing import Iterator

from utils.constant import PUZZLE_PATH

CHUNK_SIZE = 1024  # 1 kB


def to_list(file_path: str | Path, sep: str = "\n") -> Iterator[str]:
    """Read a file and yield its content split by the given separator."""
    buffer = ""
    with open(file_path, "r") as file:
        while True:
            chunk = file.read(CHUNK_SIZE)
            if not chunk:
                if buffer != "":
                    yield buffer
                return
            # When separator is not newline, remove newlines from chunk
            if sep != "\n":
                chunk = chunk.replace("\n", "")
            buffer += chunk
            while True:
                try:
                    part, buffer = buffer.split(sep, 1)
                except ValueError:
                    break
                else:
                    yield part


def input_path(day: int) -> Path:
    """Construct the file path for the input data of a given year and day."""
    return Path(PUZZLE_PATH) / "2025" / f"{day:02d}" / "input.txt"
