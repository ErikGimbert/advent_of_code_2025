from typing import Any

import pytest

from src.utils.file import to_list
from tests.utils import with_tmp_file


def test_file_to_list1():
    def f(file_path: str) -> Any:
        # Call the function to test
        result = list(to_list(file_path))

        # Assert the result
        assert result == ["line1", "line2", "line3"]

    with_tmp_file("line1\nline2\nline3\n")(f)()


def test_file_to_list2():
    def f(file_path: str) -> Any:
        # Call the function to test
        result = list(to_list(file_path, sep=","))

        # Assert the result
        assert result == [
            "11-22",
            "95-115",
            "998-1012",
            "1188511880-1188511890",
            "222220-222224",
            "1698522-1698528",
            "446443-446449",
            "38593856-38593862",
            "565653-565659",
            "824824821-824824827",
            "2121212118-2121212124",
        ]

    with_tmp_file("""11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124""")(f)()


@pytest.mark.parametrize(
    "content,expected",
    [
        ("11-22,33-44,\n55-66", ["11-22", "33-44", "55-66"]),
        ("11-22,33-\n44,55-66", ["11-22", "33-44", "55-66"]),
        ("11-22,3\n3-44,55-66", ["11-22", "33-44", "55-66"]),
    ],
)
def test_file_to_list3(content, expected):
    def f(file_path: str) -> Any:
        # Call the function to test
        result = list(to_list(file_path, sep=","))

        # Assert the result
        assert result == expected

    with_tmp_file(content)(f)()


def test_file_to_list_big():
    big_content = "A\n" * 5000 + "B\n" * 5000 + "C\n" * 5000

    def f(file_path: str) -> Any:
        # Call the function to test
        result = list(to_list(file_path))

        # Assert the result
        assert result.count("A") == 5000
        assert result.count("B") == 5000
        assert result.count("C") == 5000
        assert result == ["A"] * 5000 + ["B"] * 5000 + ["C"] * 5000
        assert len(result) == 15000

    with_tmp_file(big_content)(f)()
