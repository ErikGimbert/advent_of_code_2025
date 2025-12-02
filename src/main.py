import argparse

import colorama

from days import list_days, run_day


def main():
    print(
        f"\n{colorama.Fore.GREEN}Hello from 🎄 advent-of-code-2025 🎄{colorama.Style.RESET_ALL}"
    )
    loaded_days = list_days()

    # Parse args to run specific days if needed
    parser = argparse.ArgumentParser(
        description="Run Advent of Code 2025 solutions for specific days."
    )
    parser.add_argument(
        "day",
        type=int,
        nargs="?",
        help="Day number to run (1-12)",
        choices=loaded_days,
        default=loaded_days[-1],
    )
    args = parser.parse_args()

    run_day(args.day)

    print(f"\n{colorama.Fore.GREEN}🎉 All done! 🎉{colorama.Style.RESET_ALL}\n")


if __name__ == "__main__":
    main()
