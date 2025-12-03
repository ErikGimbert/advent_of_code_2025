import pytest  # noqa: F401

from days.d03 import load_data, p1_max_joltage, p2_max_joltage
from tests.utils import with_tmp_file

# ===========================================================================
# MARK: Part One
# ===========================================================================


class TestLoadData:
    def test_load_data(self):
        def f(file_path: str) -> None:
            result = list(load_data(file_path))
            assert result == [
                "987654321111111",
                "811111111111119",
                "234234234234278",
                "818181911112111",
            ]

        with_tmp_file("""987654321111111
811111111111119
234234234234278
818181911112111
""")(f)()


class TestP1:
    EXAMPLE_BANKS_WITH_MAX_JOLTAGE = [
        ("987654321111111", 98),
        ("811111111111119", 89),
        ("234234234234278", 78),
        ("818181911112111", 92),
    ]
    TOTAL_EXPECTED = 357

    @pytest.mark.parametrize(
        "bank, expected",
        EXAMPLE_BANKS_WITH_MAX_JOLTAGE,
    )
    def test_max_joltage(self, bank, expected):
        assert p1_max_joltage(bank) == expected

    def test_max_joltage_all_same(self):
        bank = "1111111"
        expected = 11  # tens=1, unit=1 -> 1*10 + 1 = 11
        assert p1_max_joltage(bank) == expected

    def test_sum_of_max_joltage(self):
        total = 0
        for bank, _ in self.EXAMPLE_BANKS_WITH_MAX_JOLTAGE:
            res = p1_max_joltage(bank)
            total += res
        assert total == self.TOTAL_EXPECTED


# ===========================================================================
# MARK: Part Two
# ===========================================================================


class TestP2:
    EXAMPLE_BANKS_WITH_MAX_JOLTAGE = [
        ("987654321111111", 987654321111),
        ("811111111111119", 811111111119),
        ("234234234234278", 434234234278),
        ("818181911112111", 888911112111),
    ]
    TOTAL_EXPECTED = 3121910778619

    @pytest.mark.parametrize(
        "bank, expected",
        EXAMPLE_BANKS_WITH_MAX_JOLTAGE,
    )
    def test_max_joltage(self, bank, expected):
        assert p2_max_joltage(bank) == expected

    def test_max_joltage_all_same(self):
        bank = "111111111111111"
        expected = int("1" * 12)
        assert p2_max_joltage(bank) == expected

    def test_sum_of_max_joltage(self):
        total = 0
        for bank, _ in self.EXAMPLE_BANKS_WITH_MAX_JOLTAGE:
            res = p2_max_joltage(bank)
            total += res
        assert total == self.TOTAL_EXPECTED
