from random import randint

import colorama

DECORATION = ["🍪", "🍩", "🎂", "🧁", "🍰", "🦌", "🎅", "🤶", "🎁", "❄️ ", "🌟"]


def pr_info(message: str) -> None:
    """Print an informational message in a standardized format.

    Args:
        message (str): The message to print.
    """
    decoration = DECORATION[randint(0, len(DECORATION) - 1)]
    print(f"{decoration} {message}")


def pr_day(day: int, message: str) -> None:
    """Print a message for a given day in a standardized format.

    Args:
        day (int): The day number.
        message (str): The message to print.
    """
    pr_info(f"{colorama.Fore.GREEN}Day {day}:{colorama.Style.RESET_ALL} {message}")


if __name__ == "__main__":
    print("All decorations:", DECORATION)
    pr_info("This is an informational message.")
    pr_day(1, "This is a message for day 1.")
