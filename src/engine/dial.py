import re

_RE_COMMAND = re.compile(r"^(L|R)([0-9]+)$")


class Dial:
    """A simple dial that can be turned left or right by a specified number of units."""

    __value: int
    """Current value of the dial."""
    __count_zeros: int
    """Number of times the dial has crossed on zero."""
    __count_zeros_ending: int
    """Number of times the dial has landed on zero."""

    def __init__(self, initial_value: int = 0):
        self.__value = initial_value
        self.__count_zeros = 0
        self.__count_zeros_ending = 0

    @property
    def value(self) -> int:
        """Get the current value of the dial."""
        return self.__value

    @property
    def count_zeros(self) -> int:
        """Get the number of times the dial has crossed on zero."""
        return self.__count_zeros

    @property
    def count_zeros_ending(self) -> int:
        """Get the number of times the dial has landed on zero."""
        return self.__count_zeros_ending

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
        mod_units = units % 100

        # Turn the dial
        if direction == "L":
            self.__value -= mod_units
        elif direction == "R":
            self.__value += mod_units
        # Wrap around the dial
        self.__value %= 100

        # Count zeros
        if self.__value == 0:
            self.__count_zeros_ending += 1
            self.__count_zeros += 1
        else:
            # Check if we crossed zero
            if direction == "L" and self.__value > 100 - mod_units:
                self.__count_zeros += 1
            elif direction == "R" and self.__value < mod_units:
                self.__count_zeros += 1
        if units >= 100:
            self.__count_zeros += units // 100
