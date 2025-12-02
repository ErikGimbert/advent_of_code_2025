from dial import Dial
from utils.file import file_to_commands


def day1():
    commands = file_to_commands("./inputs/day_01.txt")
    dial = Dial(50)
    for command in commands:
        dial.turn(command)
    print(f"Day 1: Dial crossed zero {dial.count_zeros} times.")


def main():
    print("Hello from advent-of-code-2025!")
    day1()


if __name__ == "__main__":
    main()
