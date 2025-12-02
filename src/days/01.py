from engine.dial import Dial
from utils.file import file_to_commands
from utils.print import pr_day


def day01():
    commands = file_to_commands("./inputs/day_01.txt")
    dial = Dial(50)
    for command in commands:
        dial.turn(command)
    pr_day(1, f"Dial crossed zero {dial.count_zeros} times.")


day01()
