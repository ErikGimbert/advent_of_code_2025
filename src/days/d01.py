from engine.dial import Dial
from utils.file import file_to_list
from utils.print import pr_day


def run():
    commands = file_to_list("./inputs/day_01.txt")
    dial = Dial(50)
    for command in commands:
        dial.turn(command)
    pr_day(1, "Part One: Dial ended zero", dial.count_zeros_ending, "times.")
    pr_day(1, "Part Two: Dial crossed zero", dial.count_zeros, "times.")
