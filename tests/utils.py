import os
import tempfile
from functools import wraps
from typing import Callable


def with_tmp_file(content: str):
    """Context manager to create and clean up a temporary file."""

    def decorator(func: Callable[[str], None]) -> Callable[[], None]:
        @wraps(func)
        def wrapper() -> None:
            tmp_file = None
            try:
                with tempfile.NamedTemporaryFile(delete=False, mode="w") as tmp_file:
                    tmp_file.write(content)
                    tmp_file.close()
                    file_path = tmp_file.name
                func(file_path)
            finally:
                if tmp_file:
                    os.remove(tmp_file.name)

        return wrapper

    return decorator
