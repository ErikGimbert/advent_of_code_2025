import re

_RE_COMMAND = re.compile(r"^(L|R)([0-9]+)$")


class Dial:
    """A simple dial that can be turned left or right by a specified number of units."""

    __value: int
    __count_zeros: int

    def __init__(self, initial_value: int = 0):
        self.__value = initial_value
        self.__count_zeros = 0

    @property
    def value(self) -> int:
        """Get the current value of the dial."""
        return self.__value

    @property
    def count_zeros(self) -> int:
        """Get the number of times the dial has landed on zero."""
        return self.__count_zeros

    def turn(self, command: str):
        """Turn the dial based on the command.
        Commands can be 'L3' or 'R56' where X is the number of units to turn between 1 and 99.
        """
        # Validate command
        match = _RE_COMMAND.match(command)
        if not match:
            raise ValueError(f"Invalid command: {command}")

        # Parse command
        direction, units_str = match.groups()
        units = int(units_str)

        # Turn the dial
        if direction == "L":
            self.__value -= units
        elif direction == "R":
            self.__value += units
        # Wrap around the dial
        self.__value %= 100

        # Count zeros
        if self.__value == 0:
            self.__count_zeros += 1
