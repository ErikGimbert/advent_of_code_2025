from typing import NamedTuple

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
        assert self.dial.count_zeros == 3
