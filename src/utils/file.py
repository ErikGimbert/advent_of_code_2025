from typing import Iterator

CHUNK_SIZE = 1024  # 1 kB


def file_to_list(file_path: str, sep: str = "\n") -> Iterator[str]:
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
