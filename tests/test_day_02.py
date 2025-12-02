import pytest

from days.d02 import (
    find_invalid_ids,
    find_invalid_ids_v2,
    load_data,
    sum_invalid_ids,
    sum_invalid_ids_v2,
)
from tests.utils import with_tmp_file


class TestLoadData:
    def test_load_data(self):
        def f(file_path: str) -> None:
            result = list(load_data(file_path))
            assert result == [
                (11, 22),
                (95, 115),
                (998, 1012),
                (1188511880, 1188511890),
                (222220, 222224),
                (1698522, 1698528),
                (446443, 446449),
                (38593856, 38593862),
                (565653, 565659),
                (824824821, 824824827),
                (2121212118, 2121212124),
            ]

        with_tmp_file("""11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
    1698522-1698528,446443-446449,38593856-38593862,565653-565659,
    824824821-824824827,2121212118-2121212124""")(f)()

    @pytest.mark.parametrize(
        "content",
        [
            "11-22,33-44,invalid,55-66",
            "11-22,33-44,55-66-77",
            "11-22,33-44,NaN-55",
        ],
    )
    def test_load_data_invalid(self, content: str):
        def f(file_path: str) -> None:
            try:
                list(load_data(file_path))
                assert False, "Expected ValueError"
            except ValueError as e:
                assert "Invalid range" in str(e)

        with_tmp_file(content)(f)()


RANGES_WITH_INVALID_IDS = [
    ((11, 22), [11, 22]),
    ((95, 115), [99]),
    ((998, 1012), [1010]),
    ((1188511880, 1188511890), [1188511885]),
    ((222220, 222224), [222222]),
    ((1698522, 1698528), []),
    ((446443, 446449), [446446]),
    ((38593856, 38593862), [38593859]),
    ((565653, 565659), []),
    ((824824821, 824824827), []),
    ((2121212118, 2121212124), []),
]


class TestFindInvalidIds:
    @pytest.mark.parametrize(
        "ids_range,expected",
        RANGES_WITH_INVALID_IDS,
    )
    def test_find_invalid_ids(self, ids_range, expected):
        result = list(find_invalid_ids(ids_range))
        assert result == expected


class TestSumInvalidIds:
    def test_sum_invalid_ids(self):
        ids_ranges = []
        expected_sum = 0
        for ids_range, invalid_ids in RANGES_WITH_INVALID_IDS:
            ids_ranges.append(ids_range)
            expected_sum += sum(invalid_ids)

        result = sum_invalid_ids(iter(ids_ranges))
        assert result == expected_sum
        assert result == 1227775554


# ==============================================================
# Part Two
# ==============================================================


RANGES_WITH_INVALID_IDS_V2 = [
    ((11, 22), [11, 22]),
    ((95, 115), [99, 111]),
    ((998, 1012), [999, 1010]),
    ((1188511880, 1188511890), [1188511885]),
    ((222220, 222224), [222222]),
    ((1698522, 1698528), []),
    ((446443, 446449), [446446]),
    ((38593856, 38593862), [38593859]),
    ((565653, 565659), [565656]),
    ((824824821, 824824827), [824824824]),
    ((2121212118, 2121212124), [2121212121]),
]


class TestFindInvalidIdsV2:
    @pytest.mark.parametrize(
        "ids_range,expected",
        RANGES_WITH_INVALID_IDS_V2,
    )
    def test_find_invalid_ids_v2(self, ids_range, expected):
        result = list(find_invalid_ids_v2(ids_range))
        assert result == expected


class TestSumInvalidIdsV2:
    def test_sum_invalid_ids_v2(self):
        ids_ranges = []
        expected_sum = 0
        for ids_range, invalid_ids in RANGES_WITH_INVALID_IDS_V2:
            ids_ranges.append(ids_range)
            expected_sum += sum(invalid_ids)

        result = sum_invalid_ids_v2(iter(ids_ranges))
        assert result == expected_sum
        assert result == 4174379265
