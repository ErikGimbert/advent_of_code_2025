import re
from pathlib import Path

from utils.print import pr_info


def list_days() -> list[int]:
    """List all available days by scanning the current directory for day files."""
    loaded_days: list[int] = []
    re_day = re.compile(r"(\d{2})")
    for f in Path(__file__).parent.glob("*.py"):
        if f.stem != "__init__" and re_day.fullmatch(f.stem) is not None:
            loaded_days.append(int(f.stem))
    loaded_days.sort()
    return loaded_days


def run_day(day: int) -> None:
    """Run the specified day's function."""
    pr_info(f"Running Day {day}...\n")
    __import__(f"days.{day:02}")
