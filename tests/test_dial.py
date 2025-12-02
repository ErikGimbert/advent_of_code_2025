from typing import NamedTuple

import pytest

from dial import Dial


class TestDialSimple:
    dial = Dial(11)

    def test_right_8(self):
        self.dial.turn("R8")
        assert self.dial.value == 19

    def test_left_19(self):
        self.dial.turn("L19")
        assert self.dial.value == 0


class TestDialMoreSimple:
    def test_right_0(self):
        dial = Dial(25)
        dial.turn("R0")
        assert dial.value == 25

    def test_right_876(self):
        dial = Dial(25)
        dial.turn("R826")
        assert dial.value == 51


class TestDialCircle:
    dial = Dial(0)

    def test_left_0(self):
        self.dial.turn("L1")
        assert self.dial.value == 99

    def test_right_1(self):
        self.dial.turn("R1")
        assert self.dial.value == 0


class TestDialMoreCircle:
    dial = Dial(5)

    def test_left_10(self):
        self.dial.turn("L10")
        assert self.dial.value == 95

    def test_right_5(self):
        self.dial.turn("R5")
        assert self.dial.value == 0


class TestDialInvalid:
    dial = Dial(50)

    def test_invalid_direction(self):
        try:
            self.dial.turn("X10")
        except ValueError as e:
            assert str(e) == "Invalid command: X10"
        else:
            assert False, "Expected ValueError for invalid direction"


Turn = NamedTuple("Turns", [("command", str), ("expected_value", int)])


class TestDialMultipleTurns:
    dial = Dial(50)
    turns: list[Turn] = [
        Turn("L68", 82),
        Turn("L30", 52),
        Turn("R48", 0),
        Turn("L5", 95),
        Turn("R60", 55),
        Turn("L55", 0),
        Turn("L1", 99),
        Turn("L99", 0),
        Turn("R14", 14),
        Turn("L82", 32),
    ]

    def test_multiple_turns(self):
        for turn in self.turns:
            self.dial.turn(turn.command)
            assert self.dial.value == turn.expected_value

    def test_count_zeros(self):
        assert self.dial.count_zeros_ending == 3


# ===========================================================================
# MARK: Part Two
# ===========================================================================


class TestDial2MultipleTurns:
    dial = Dial(50)
    turns: list[Turn] = [
        Turn("L68", 82),
        Turn("L30", 52),
        Turn("R48", 0),
        Turn("L5", 95),
        Turn("R60", 55),
        Turn("L55", 0),
        Turn("L1", 99),
        Turn("L99", 0),
        Turn("R14", 14),
        Turn("L82", 32),
    ]

    def test_multiple_turns(self):
        for turn in self.turns:
            self.dial.turn(turn.command)
            assert self.dial.value == turn.expected_value

    def test_count_zeros(self):
        assert self.dial.count_zeros == 6


class TestDial2CircleCrossing:
    @pytest.mark.parametrize(
        "initial,command,expected_value,expected_zeros",
        [
            (50, "L1000", 50, 10),
            (50, "R951", 1, 10),
            (50, "R950", 0, 10),
            (50, "R949", 99, 9),
            (25, "L524", 1, 5),
            (25, "L525", 0, 6),
            (25, "L526", 99, 6),
        ],
    )
    def test(self, initial, command, expected_value, expected_zeros):
        dial = Dial(initial)
        dial.turn(command)
        assert dial.value == expected_value
        assert dial.count_zeros == expected_zeros
