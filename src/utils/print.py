from random import randint
from typing import Optional, overload

import colorama

DECORATION = ["🍪", "🍩", "🎂", "🧁", "🍰", "🦌", "🎅", "🤶", "🎁", "❄️ ", "🌟"]


def pr_info(message: str) -> None:
    """Print an informational message in a standardized format.

    Args:
        message (str): The message to print.
    """
    decoration = DECORATION[randint(0, len(DECORATION) - 1)]
    print(f"{decoration} {message}")


@overload
def pr_day(day: int, message: str) -> None:
    """Print a message for a given day in a standardized format.

    Args:
        day (int): The day number.
        message (str): The message to print.
    """
    ...


@overload
def pr_day(day: int, message: str, answer: int, post_answer: str = "") -> None:
    """Print a message for a given day in a standardized format.

    Args:
        day (int): The day number.
        message (str): The message before the answer.
        answer (int): The answer to print.
        post_answer (Optional[str]): The message after the answer.
    """
    ...


def pr_day(
    day: int,
    message: str,
    answer: Optional[int] = None,
    post_answer: Optional[str] = "",
) -> None:
    if answer is None:
        pr_info(f"{colorama.Fore.GREEN}Day {day}:{colorama.Style.RESET_ALL} {message}")
    else:
        pr_info(
            f"{colorama.Fore.GREEN}Day {day}:{colorama.Style.RESET_ALL} {message}"
            + f" {colorama.Fore.CYAN}{colorama.Style.BRIGHT}{answer}{colorama.Style.RESET_ALL} {post_answer}"
        )


if __name__ == "__main__":
    print("All decorations:", DECORATION)
    pr_info("This is an informational message.")
    pr_day(1, "This is a message for day 1,", 42, "is the answer.")
